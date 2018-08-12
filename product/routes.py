from flask import Blueprint, render_template
import os

product_api = Blueprint('product_api', __name__, template_folder='templates')

@product_api.route('/')
def show():
    return render_template('products.html')