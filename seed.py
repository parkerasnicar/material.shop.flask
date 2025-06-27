from main import app, db
from models import Product

# Sample data
sample_products = [
    {
        "name": "Organic Cotton Hoodie",
        "description": "A cozy hoodie made from 100% organic cotton.",
        "category": "Hoodies",
        "price": 69.99,
        "stock": 20,
        "brand": "EcoThreads",
        "sustainability_rating": "A+",
        "available_sizes": "S,M,L,XL",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Vintage Denim Jacket",
        "description": "A classic denim jacket with a vintage finish.",
        "category": "Jackets",
        "price": 89.99,
        "stock": 15,
        "brand": "DenimWorks",
        "sustainability_rating": "B",
        "available_sizes": "M,L,XL",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Eco-Friendly T-Shirt",
        "description": "Soft and breathable t-shirt made from bamboo fibers.",
        "category": "Shirts",
        "price": 29.99,
        "stock": 50,
        "brand": "GreenWear",
        "sustainability_rating": "A",
        "available_sizes": "S,M,L",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Recycled Polyester Pants",
        "description": "Durable and stylish pants made from recycled materials.",
        "category": "Pants",
        "price": 59.99,
        "stock": 30,
        "brand": "ReFashion",
        "sustainability_rating": "A",
        "available_sizes": "M,L,XL",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Sustainable Canvas Sneakers",
        "description": "Comfortable sneakers made with eco-friendly materials.",
        "category": "Footwear",
        "price": 79.99,
        "stock": 25,
        "brand": "SoleMate",
        "sustainability_rating": "A+",
        "available_sizes": "7,8,9,10,11,12",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Organic Linen Shirt",
        "description": "A breathable linen shirt, perfect for summer days.",
        "category": "Shirts",
        "price": 49.99,
        "stock": 40,
        "brand": "NatureWear",
        "sustainability_rating": "A",
        "available_sizes": "S,M,L,XL",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Recycled Nylon Backpack",
        "description": "Stylish and durable backpack made from recycled nylon.",
        "category": "Accessories",
        "price": 99.99,
        "stock": 10,
        "brand": "EcoPack",
        "sustainability_rating": "A+",
        "available_sizes": "One Size",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Upcycled Denim Shorts",
        "description": "Trendy shorts crafted from upcycled denim.",
        "category": "Shorts",
        "price": 39.99,
        "stock": 35,
        "brand": "DenimWorks",
        "sustainability_rating": "B+",
        "available_sizes": "S,M,L",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Handcrafted Wool Beanie",
        "description": "Cozy and stylish beanie made from 100% wool.",
        "category": "Accessories",
        "price": 24.99,
        "stock": 50,
        "brand": "WarmHues",
        "sustainability_rating": "A",
        "available_sizes": "One Size",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Vegan Leather Jacket",
        "description": "A bold and cruelty-free leather jacket for a modern look.",
        "category": "Jackets",
        "price": 129.99,
        "stock": 12,
        "brand": "VeganEdge",
        "sustainability_rating": "A+",
        "available_sizes": "M,L,XL",
        "image_url": "https://via.placeholder.com/200"
    },
    {
        "name": "Bamboo Fiber Socks",
        "description": "Super soft socks made from sustainable bamboo fibers.",
        "category": "Accessories",
        "price": 9.99,
        "stock": 100,
        "brand": "GreenStep",
        "sustainability_rating": "A",
        "available_sizes": "One Size",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Eco-Dyed Hoodie",
        "description": "Hoodie dyed using eco-friendly processes for a natural look.",
        "category": "Hoodies",
        "price": 74.99,
        "stock": 18,
        "brand": "EcoThreads",
        "sustainability_rating": "A",
        "available_sizes": "S,M,L,XL",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Vintage Cargo Pants",
        "description": "Comfortable cargo pants with a vintage design.",
        "category": "Pants",
        "price": 64.99,
        "stock": 22,
        "brand": "RetroStyle",
        "sustainability_rating": "B+",
        "available_sizes": "M,L,XL",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Organic Cotton Tote Bag",
        "description": "Reusable tote bag made from organic cotton.",
        "category": "Accessories",
        "price": 14.99,
        "stock": 60,
        "brand": "CarryKind",
        "sustainability_rating": "A+",
        "available_sizes": "One Size",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Recycled Wool Scarf",
        "description": "Warm scarf made from recycled wool.",
        "category": "Accessories",
        "price": 34.99,
        "stock": 25,
        "brand": "WarmHues",
        "sustainability_rating": "A",
        "available_sizes": "One Size",
        "image_url": "https://placehold.co/500"
    },
    {
        "name": "Sustainable Cotton Joggers",
        "description": "Joggers made from sustainably grown cotton for everyday comfort.",
        "category": "Pants",
        "price": 49.99,
        "stock": 40,
        "brand": "EcoComfort",
        "sustainability_rating": "A+",
        "available_sizes": "S,M,L,XL",
        "image_url": "https://placehold.co/500"
    }
]

with app.app_context():
    # Clear existing data
    db.session.query(Product).delete()

    # Add sample products
    for product in sample_products:
        new_product = Product(
            name=product["name"],
            description=product["description"],
            category=product["category"],
            price=product["price"],
            stock=product["stock"],
            brand=product["brand"],
            sustainability_rating=product["sustainability_rating"],
            available_sizes=product["available_sizes"],
            image_url=product["image_url"]
        )
        db.session.add(new_product)

    db.session.commit()
    print("Sample data added successfully!")