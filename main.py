from flask import Flask, request, render_template, url_for
from db import db
from models import Product, ProductImage, Order, OrderDetail

app = Flask(__name__)
# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///material_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Homepage Route
@app.route('/')
def index():
    # Fetch all products and highlight a specific product
    products = Product.query.all()
    hot_product = Product.query.filter_by(name="Organic Cotton Hoodie").first()

    return render_template('index.html', products=products, hot_product=hot_product)

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Shop Page Route
@app.route('/shop', methods=['GET'])
def shop():
    # Fetch filters and pagination details from the request
    search_query = request.args.get('search', '').strip()
    category_filter = request.args.getlist('category')  # Support for multiple categories
    page = request.args.get('page', 1, type=int)

    # Start with the base query for products
    query = Product.query

    # Apply search filter if provided
    if search_query:
        query = query.filter(Product.name.ilike(f"%{search_query}%"))

    # Apply category filter if selected
    if category_filter:
        query = query.filter(Product.category.in_(category_filter))

    # Paginate the filtered results (8 items per page)
    products = query.paginate(page=page, per_page=8)

    return render_template(
        'shop.html',
        products=products.items,
        pagination=products,
        search_query=search_query,
        selected_categories=category_filter
    )

# Product Details Route
@app.route('/shop/<category>/<int:item_id>')
def item_details(category, item_id):
    # Fetch product by its ID or return a 404 error if not found
    product = Product.query.get_or_404(item_id)

    # Temporary stock data (replace with actual logic)
    stock_by_size = {
        "S": 5,   # Small in stock
        "M": 0,   # Medium out of stock
        "L": 3,   # Large in stock
        "XL": 2,  # XL in stock
        "One Size": 2
    }

    # Inject stock data into the product object
    product.stock_by_size = stock_by_size

    return render_template('item-details.html', product=product)

# Cart Page Route
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Checkout Page Route
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Main Execution
if __name__ == '__main__':
    # Initialize the database before running the app
    with app.app_context():
        db.create_all()
        print("Database initialized!")
    app.run(debug=True)

# Recreate the database
with app.app_context():
    db.create_all()
    print("Database has been created successfully!")