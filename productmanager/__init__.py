from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '318896901b51ce7c2448939cac888e64'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from productmanager.routes import home_api
from productmanager.product.routes import product_api
from productmanager.user.routes import user_api

app.register_blueprint(product_api, url_prefix='/products')
app.register_blueprint(home_api, url_prefix='/')
app.register_blueprint(user_api, url_prefix="/user")

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404