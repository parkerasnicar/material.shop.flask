from flask import Flask, request, render_template
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

@app.route('/shop')
def shop():
    page = request.args.get('page', 1, type=int)
    per_page = 8  # Number of items per page
    query = Product.query  # Base query

    # Handle category filter
    category = request.args.get('category')
    if category:
        query = query.filter_by(category=category)

    # Handle search
    search_query = request.args.get('search')
    if search_query:
        query = query.filter(Product.name.ilike(f"%{search_query}%"))

    # Paginate query
    pagination = query.paginate(page=page, per_page=per_page)
    products = pagination.items

    return render_template('shop.html', products=products, pagination=pagination)

@app.route('/shop/<category>/<int:item_id>')
def item_details(category, item_id):
    # Query the product based on its ID
    product = Product.query.get_or_404(item_id)
    
    # Ensure the product's category matches the URL
    if product.category.lower() != category.lower():
        return redirect(url_for('shop'))  # Redirect to shop page if mismatch

    # Render the item details page
    return render_template('item_details.html', product=product)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database initialized!")
    app.run(debug=True)

# Recreate the database
with app.app_context():
    db.create_all()
    print("Database has been created successfully!")