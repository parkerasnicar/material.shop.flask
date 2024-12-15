from datetime import datetime
from db import db

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    brand = db.Column(db.String(100), nullable=True)
    sustainability_rating = db.Column(db.String(20), nullable=True)
    available_sizes = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    images = db.relationship('ProductImage', backref='product', lazy=True)
    order_details = db.relationship('OrderDetail', backref='product', lazy=True)

# Additional Images for Products
class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Customer Orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime)
    shipping_address = db.Column(db.Text)
    order_details = db.relationship('OrderDetail', backref='order', lazy=True)

# Details of Products in an Order
class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price_at_purchase = db.Column(db.Float, nullable=False)