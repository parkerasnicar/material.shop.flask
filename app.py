from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///material_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Make sure this is db = SQLAlchemy(app) and not just db = SQLAlchemy()

from models import Product, ProductImage, Order, OrderDetail  # Import models after db is set up

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # instead of returning "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)