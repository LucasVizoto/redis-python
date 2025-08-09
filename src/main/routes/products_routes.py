from flask import Blueprint, jsonify

product_routes_bp = Blueprint("products_routes", __name__)

@product_routes_bp.route("/products", methods=['POST'])
def insert_product():
    return jsonify({"message":"cadastrado com sucesso"}), 200

@product_routes_bp.route("/products/<product_name>", methods=['GET'])
def get_product_by_name(product_name):
    return jsonify({"message": f"product {product_name}"}), 200