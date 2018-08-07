from flask import Flask, Blueprint
from product import routes

app = Flask(__name__)

app.register_blueprint(routes.product_api, url_prefix='/products')

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)