from productmanager import db
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required
from productmanager.product.forms import ProductRegisterForm
from productmanager.product.models import Product

product_api = Blueprint('product_api', __name__, template_folder='templates')

@product_api.route('/')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.date_created.desc()).paginate(page=page, per_page=5)
    return render_template('products.html', products=products)

@product_api.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = ProductRegisterForm()

    if form.validate_on_submit():
        product = Product(form.name.data, form.description.data)
        db.session.add(product)
        db.session.commit()
        flash('Product created with successs!', 'success')
        return redirect(url_for('product_api.home'))

    return render_template('registerproduct.html', title='Register Product', form = form)