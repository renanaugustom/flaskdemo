from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from productmanager.product.routes import product_api

app = Flask(__name__)
app.config['SECRET_KEY'] = '318896901b51ce7c2448939cac888e64'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)

app.register_blueprint(product_api, url_prefix='/products')
from productmanager.routes import home_api
app.register_blueprint(home_api, url_prefix='/')

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404