from flask import Blueprint

product_api = Blueprint('product_api', __name__)

@product_api.route('/')
def show():
    return 'Products'