# SQLAlchemy data models for Category and Product

from db import db

class Category(db.Model):
    """
    Represents a product category (e.g., Laptops, Printers) scraped from BestBuy.
    """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for the category (auto-incremented)
    name = db.Column(db.String(255), unique=True, nullable=False)  # Category name (must be unique)
    url = db.Column(db.Text, unique=True, nullable=False)  # URL to the category page

    # Relationship: A category has many products
    products = db.relationship('Product', backref='category', cascade='all, delete', lazy=True)

    def serialize(self):
        """
        Returns a dictionary representation of the Category instance.
        Useful for API responses.
        """
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }


class Product(db.Model):
    """
    Represents an individual product listed under a specific category on BestBuy.
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for the product (auto-incremented)
    name = db.Column(db.String(255), nullable=False)  # Product name/title
    price = db.Column(db.String(50))  # Product price as displayed (stored as string for formatting)
    rating = db.Column(db.Float)  # Product rating (can be null if no rating available)

    # Foreign key to associate product with a category
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'))

    def serialize(self):
        """
        Returns a dictionary representation of the Product instance.
        Includes the category name for display in the frontend.
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'category': self.category.name if self.category else None
        }
