from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret_key_123"  # مفتاح سري علشان السيشن

# بيانات منتجات تجريبية
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 150}
]

# الصفحة الرئيسية
@app.route("/")
def index():
    return render_template("index.html", products=products)

# صفحة تسجيل الدخول
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect(url_for("index"))
    return render_template("login.html")

# إضافة للسلة
@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product_id)
    return redirect(url_for("cart"))

# عرض السلة
@app.route("/cart")
def cart():
    if "cart" not in session:
        session["cart"] = []
    cart_items = [p for p in products if p["id"] in session["cart"]]
    return render_template("cart.html", cart=cart_items)

if __name__ == "__main__":
    app.run(debug=True)
