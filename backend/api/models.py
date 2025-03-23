# SQLAlchemy data models (Product, Category)

from . import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    url = db.Column(db.Text, unique=True, nullable=False)

    products = db.relationship('Product', backref='category', cascade='all, delete', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(50))
    rating = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'category': self.category.name if self.category else None
        }
