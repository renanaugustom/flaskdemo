from flask import Flask, Blueprint, url_for
from product import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = '318896901b51ce7c2448939cac888e64'

app.register_blueprint(routes.product_api, url_prefix='/products')

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)