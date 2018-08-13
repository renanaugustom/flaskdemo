from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from productmanager.product import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = '318896901b51ce7c2448939cac888e64'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)

app.register_blueprint(routes.product_api, url_prefix='/products')
from productmanager import routes
