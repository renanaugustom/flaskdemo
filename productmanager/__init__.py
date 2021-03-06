from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '318896901b51ce7c2448939cac888e64'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home_api.login'
login_manager.login_message_category = 'danger'

from productmanager import models

from productmanager.main.routes import home_api
from productmanager.product.routes import product_api
from productmanager.user.routes import user_api

app.register_blueprint(product_api, url_prefix='/products')
app.register_blueprint(home_api, url_prefix='/')
app.register_blueprint(user_api, url_prefix="/user")

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404