from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/category")
def category():
    return render_template("category.html")


@app.route("/product_detail")
def product_detail():
    return render_template("product_detail.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")