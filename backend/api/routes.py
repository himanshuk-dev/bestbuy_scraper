# API route definitions for product and category endpoints

from flask import Blueprint, jsonify, request, current_app
from db import db
from models import Product, Category

# Create a blueprint for API routes under the prefix /data
api_bp = Blueprint('api', __name__, url_prefix='/data')


# Helper function to paginate a SQLAlchemy query
def paginate(query, page, per_page):
    return query.paginate(page=page, per_page=per_page, error_out=False)


# GET /data
# Fetch all products with pagination support
@api_bp.route('/', methods=['GET'])
def get_all_products():
    # Get query parameters for pagination (default page=1, per_page=10)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Paginate all products
    paginated = paginate(Product.query, page, per_page)
    products = [product.serialize() for product in paginated.items]

    # Return paginated response as JSON
    return jsonify({
        "products": products,
        "total": paginated.total,
        "page": paginated.page,
        "pages": paginated.pages
    })


# GET /data/categories
# Returns a list of all available category names
@api_bp.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    return jsonify([cat.name for cat in categories])


# GET /data/category/<category_name>
# Returns products filtered by a specific category
@api_bp.route('/category/<string:category_name>', methods=['GET'])
def get_products_by_category(category_name):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Fetch the category object from the DB
    category = Category.query.filter_by(name=category_name).first()
    if not category:
        return jsonify({"error": "Category not found"}), 404

    # Filter products by this category ID and paginate
    query = Product.query.filter_by(category_id=category.id)
    paginated = paginate(query, page, per_page)
    products = [product.serialize() for product in paginated.items]

    return jsonify({
        "products": products,
        "total": paginated.total,
        "page": paginated.page,
        "pages": paginated.pages
    })


# DELETE /data/<id>
# Deletes a product by its ID
@api_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    with current_app.app_context():
        session = db.session

        # Attempt to retrieve the product by ID
        product = session.get(Product, id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Delete the product and commit the transaction
        session.delete(product)
        session.commit()

        return jsonify({"message": f"Product {id} deleted successfully."})
