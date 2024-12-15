from flask import Flask, render_template, request
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///material_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Import models after db is set up
from models import Product, ProductImage, Order, OrderDetail

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/shop')
def shop():
    """
    Shop page that displays all products by default.
    Filters products by category if a 'category' parameter is provided.
    """
    category = request.args.get('category')  # Retrieve category filter from query parameters
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/item/<int:product_id>')
def item_details(product_id):
    """
    Product details page for a specific product.
    """
    product = Product.query.get_or_404(product_id)  # Fetch product or return 404 if not found
    return render_template('item_details.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)