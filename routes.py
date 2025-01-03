# service/routes.py

from flask import Blueprint, request, jsonify
from app.models import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product.create(**data)
    return jsonify(product.to_dict()), 201

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.find(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product.update(**data)
    return jsonify(product.to_dict())

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.find(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product.delete()
    return '', 204

@product_bp.route('/products', methods=['GET'])
def list_all_products():
    products = Product.list_all()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/products', methods=['GET'])
def find_product_by_name_or_category():
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')
    
    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif availability:
        products = Product.find_by_availability(availability)
    else:
        products = Product.list_all()

    return jsonify([product.to_dict() for product in products])

