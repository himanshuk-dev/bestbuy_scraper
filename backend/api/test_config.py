# backend/api/conftest.py
import os
import pytest
from backend.api import create_app, db
from backend.api.models import Category, Product
from dotenv import load_dotenv

load_dotenv(".env.test")  # Load test environment variables

@pytest.fixture(scope="session")
def test_app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.getenv("DATABASE_URL"),
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.app_context():
        db.create_all()

        # Insert sample categories and products
        category1 = Category(name="TestCategory1", url="https://test1.com")
        category2 = Category(name="TestCategory2", url="https://test2.com")
        db.session.add_all([category1, category2])
        db.session.commit()

        product1 = Product(name="Test Product A", price="$99", rating=4.5, category_id=category1.id)
        product2 = Product(name="Test Product B", price="$149", rating=3.8, category_id=category2.id)
        db.session.add_all([product1, product2])
        db.session.commit()

        yield app

        # Teardown
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(test_app):
    return test_app.test_client()