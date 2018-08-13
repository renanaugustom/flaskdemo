from flask import render_template
from productmanager import app

@app.route("/")
def hello():
    return "Hello World!"