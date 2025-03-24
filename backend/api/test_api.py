import pytest
from flask import url_for
from app import create_app
from db import db
from models import Product, Category

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_all_products(client):
    response = client.get('/data/?page=1&per_page=2')
    data = response.get_json()

    assert response.status_code == 200
    assert 'products' in data
    assert isinstance(data['products'], list)
    assert len(data['products']) <= 2


def test_get_products_by_category(client):
    response = client.get('/data/category/Computers, Tablets, & Accessories')
    data = response.get_json()

    assert response.status_code == 200
    assert 'products' in data
    for product in data['products']:
        assert product['category'] == 'Computers, Tablets, & Accessories'


def test_get_products_by_invalid_category(client):
    response = client.get('/data/category/UnknownCategory')
    data = response.get_json()

    assert response.status_code == 404
    assert 'error' in data


def test_delete_product(client):
    # First, get product ID
    response = client.get('/data/')
    data = response.get_json()
    product_id = data['products'][0]['id']

    # Delete the product
    del_response = client.delete(f'/data/{product_id}')
    del_data = del_response.get_json()

    assert del_response.status_code == 200
    assert 'message' in del_data

    # Ensure it's deleted
    verify_response = client.get('/data/')
    verify_data = verify_response.get_json()
    ids = [p['id'] for p in verify_data['products']]
    assert product_id not in ids
