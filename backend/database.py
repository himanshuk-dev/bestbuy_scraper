# Utility for PostgreSQL connection, schema initialization, and data insertion
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from a .env file for DB credentials
load_dotenv()

# Database connection configuration loaded from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def create_database_if_not_exists():
    """
    Checks if the specified database exists.
    If not, creates the database using default 'postgres' DB.
    Returns True if a new DB is created, False otherwise.
    """
    try:
        # Connect to default 'postgres' DB to perform administrative tasks
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Check if the target database already exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cur.fetchone()

        if not exists:
            # Create new database if not present
            cur.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"✅ Database '{DB_NAME}' created successfully.")
        else:
            print(f"ℹ️ Database '{DB_NAME}' already exists.")

        cur.close()
        conn.close()
        return not exists

    except Exception as e:
        print(f"❌ Error checking or creating database: {e}")
        return False

class DatabaseManager:
    """
    Handles PostgreSQL operations like initializing schema,
    inserting categories/products, and managing connections.
    """

    def __init__(self):
        self.conn = self.get_connection()

    def get_connection(self):
        """Establishes a PostgreSQL database connection using environment variables."""
        try:
            return psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def initialize_db(self):
        """
        Initializes database schema by running SQL commands
        from the 'data.sql' file.
        """
        if self.conn:
            try:
                with self.conn.cursor() as cur:
                    with open("data.sql", "r") as f:
                        cur.execute(f.read())
                self.conn.commit()
                print("Database initialized successfully.")
            except Exception as e:
                print(f"Error initializing database: {e}")

    def insert_category(self, name, url):
        """
        Inserts a new category into the 'categories' table.
        If it already exists (conflict on name), retrieves its ID.
        Returns the category ID.
        """
        if self.conn:
            try:
                with self.conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO categories (name, url)
                        VALUES (%s, %s)
                        ON CONFLICT (name) DO NOTHING
                        RETURNING id;
                        """, (name, url)
                    )
                    category_id = cur.fetchone()
                    self.conn.commit()
                    # Return the new or existing category ID
                    return category_id[0] if category_id else self.get_category_id_by_name(name)
            except Exception as e:
                print(f"Error inserting category: {e}")

    def get_category_id_by_name(self, name):
        """
        Retrieves the ID of a category by its name.
        Returns None if not found.
        """
        if self.conn:
            try:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT id FROM categories WHERE name = %s", (name,))
                    result = cur.fetchone()
                    return result[0] if result else None
            except Exception as e:
                print(f"Error fetching category ID: {e}")
                return None

    def insert_product(self, name, price, rating, category_id):
        """
        Inserts a product into the 'products' table.
        Prevents duplicate entries by checking on (name, category_id).
        """
        if self.conn:
            try:
                with self.conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO products (name, price, rating, category_id)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (name, category_id) DO NOTHING;
                        """, (name, price, rating, category_id)
                    )
                    self.conn.commit()
            except Exception as e:
                print(f"Error inserting product: {e}")

    def close_connection(self):
        """Safely closes the PostgreSQL connection."""
        if self.conn:
            self.conn.close()

# Run this file directly to initialize the database
if __name__ == "__main__":
    if create_database_if_not_exists():
        db_manager = DatabaseManager()
        db_manager.initialize_db()
        db_manager.close_connection()
