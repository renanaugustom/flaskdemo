from flask import Blueprint, render_template, flash, redirect, url_for
from productmanager.product.forms import ProductRegisterForm
import os

product_api = Blueprint('product_api', __name__, template_folder='templates')

@product_api.route('/')
def home():
    return render_template('products.html')

@product_api.route('/register', methods=['GET', 'POST'])
def register():
    form = ProductRegisterForm()

    if form.validate_on_submit():
        flash('Product created with successs!', 'success')
        return redirect(url_for('product_api.home'))

    return render_template('registerproduct.html', title='Register Product', form = form)