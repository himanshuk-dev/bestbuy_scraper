import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection settings
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def create_database_if_not_exists():
    """Creates the database if it doesn't exist. Returns True if created."""
    try:
        conn = psycopg2.connect(
            dbname="postgres",  # connect to default DB
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cur.fetchone()

        if not exists:
            cur.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"✅ Database '{DB_NAME}' created successfully.")
            cur.close()
            conn.close()
            return True
        else:
            print(f"ℹ️ Database '{DB_NAME}' already exists.")
            cur.close()
            conn.close()
            return False

    except Exception as e:
        print(f"❌ Error checking or creating database: {e}")
        return False

class DatabaseManager:
    def __init__(self):
        self.conn = self.get_connection()

    def get_connection(self):
        """Establishes and returns a PostgreSQL database connection."""
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            return conn
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def initialize_db(self):
        """Initializes the database schema from data.sql."""
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
        """Inserts a category into the database, avoiding duplicates."""
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
                    return category_id[0] if category_id else self.get_category_id_by_name(name)
            except Exception as e:
                print(f"Error inserting category: {e}")

    def get_category_id_by_name(self, name):
        """Fetches the category ID by its name."""
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
        """Inserts a product into the database, avoiding duplicates."""
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
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    if create_database_if_not_exists():
        db_manager = DatabaseManager()
        db_manager.initialize_db()
        db_manager.close_connection()
