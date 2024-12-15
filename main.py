from flask import Flask, request, render_template, url_for
from db import db
from models import Product, ProductImage, Order, OrderDetail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///material_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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

@app.route('/shop', methods=['GET'])
def shop():
    # Get search query and category filters from request arguments
    search_query = request.args.get('search', '').strip()
    category_filter = request.args.getlist('category')  # Multi-select filter support
    page = request.args.get('page', 1, type=int)

    # Start with all products
    query = Product.query

    # Apply search filter
    if search_query:
        query = query.filter(Product.name.ilike(f"%{search_query}%"))

    # Apply category filter if any
    if category_filter:
        query = query.filter(Product.category.in_(category_filter))

    # Paginate results (8 items per page)
    products = query.paginate(page=page, per_page=8)

    return render_template('shop.html', products=products.items, pagination=products, search_query=search_query, selected_categories=category_filter)

@app.route('/shop/<category>/<int:item_id>')
def item_details(category, item_id):
    product = Product.query.get_or_404(item_id)

    # Example of stock_by_size - Replace this with actual logic for your database
    stock_by_size = {
        "S": 5,   # Small in stock
        "M": 0,   # Medium out of stock
        "L": 3,   # Large in stock
        "XL": 2   # XL in stock
    }

    # Overwrite or inject this data dynamically into the product
    product.stock_by_size = stock_by_size

    return render_template('item-details.html', product=product)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database initialized!")
    app.run(debug=True)

# Recreate the database
with app.app_context():
    db.create_all()
    print("Database has been created successfully!")