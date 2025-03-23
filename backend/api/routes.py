# API route definitions

from flask import Blueprint, jsonify, request
from backend.api import db
from backend.api.models import Product, Category

api_bp = Blueprint('api', __name__, url_prefix='/data')

# Helper function for pagination
def paginate(query, page, per_page):
    return query.paginate(page=page, per_page=per_page, error_out=False)


# GET /data -> Retrieve all products with pagination
@api_bp.route('/', methods=['GET'])
def get_all_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    paginated = paginate(Product.query, page, per_page)
    products = [product.serialize() for product in paginated.items]
    return jsonify({
        "products": products,
        "total": paginated.total,
        "page": paginated.page,
        "pages": paginated.pages
    })


# GET /data/category/<category_name> -> Filter by category
@api_bp.route('/category/<string:category_name>', methods=['GET'])
def get_products_by_category(category_name):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    category = Category.query.filter_by(name=category_name).first()
    if not category:
        return jsonify({"error": "Category not found"}), 404

    query = Product.query.filter_by(category_id=category.id)
    paginated = paginate(query, page, per_page)
    products = [product.serialize() for product in paginated.items]
    return jsonify({
        "products": products,
        "total": paginated.total,
        "page": paginated.page,
        "pages": paginated.pages
    })


# DELETE /data/<int:id> -> Delete product by ID
@api_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": f"Product {id} deleted successfully."})
