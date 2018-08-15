from flask import render_template, Blueprint

home_api = Blueprint('home_api', __name__, template_folder='templates')

@home_api.route("/")
def hello():
    return "Hello World!"

@home_api.route('/login')
def login():
    return render_template('login.html')