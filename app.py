from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os

# Define the Flask app
app = Flask(__name__)

# Enable CORS for the app
CORS(app)

# Mock list of products in the database
products = [
    {"name": "Laptop", "description": "High performance laptop with 16GB RAM.", "price": 1000},
    {"name": "Smartphone", "description": "Latest model with 5G connectivity.", "price": 700},
    {"name": "Headphones", "description": "Noise-cancelling over-ear headphones.", "price": 200},
    {"name": "Smartwatch", "description": "Track your fitness and notifications.", "price": 150},
    {"name": "Tablet", "description": "10-inch tablet with high resolution display.", "price": 500},
    {"name": "Bluetooth Speaker", "description": "Portable speaker with 10-hour battery life.", "price": 90},
    {"name": "Wireless Mouse", "description": "Ergonomic wireless mouse for comfort.", "price": 30},
    {"name": "Keyboard", "description": "Mechanical keyboard with customizable keys.", "price": 50},
    {"name": "Camera", "description": "DSLR camera with 24MP sensor.", "price": 800},
    {"name": "Charger", "description": "Fast charger for smartphones and tablets.", "price": 20},
    
    {"name": "Book 1", "description": "A thrilling mystery novel.", "price": 13},
    {"name": "Book 2", "description": "A romantic love story.", "price": 16},
    {"name": "Book 3", "description": "A fascinating science fiction adventure.", "price": 10},
    {"name": "Book 4", "description": "A historical fiction based on real events.", "price": 20},
    {"name": "Book 5", "description": "A deep dive into philosophy and life.", "price": 26},
    {"name": "Book 6", "description": "A beginner’s guide to programming.", "price": 9},
    {"name": "Book 7", "description": "A motivational self-help book.", "price": 11},
    {"name": "Book 8", "description": "A biographical book of a famous entrepreneur.", "price": 19},
    {"name": "Book 9", "description": "A psychological thriller.", "price": 15},
    {"name": "Book 10", "description": "A collection of poetry.", "price": 12},
    
    {"name": "T-shirt", "description": "Cotton T-shirt with a trendy design.", "price": 20},
    {"name": "Jeans", "description": "Denim jeans with a slim fit.", "price": 50},
    {"name": "Jacket", "description": "Winter jacket with a fleece lining.", "price": 80},
    {"name": "Sneakers", "description": "Comfortable running sneakers.", "price": 60},
    {"name": "Socks", "description": "Soft and breathable cotton socks.", "price": 6},
    {"name": "Hat", "description": "Stylish cap for everyday use.", "price": 15},
    {"name": "Sweater", "description": "Knitted sweater for cold weather.", "price": 35},
    {"name": "Scarf", "description": "Warm scarf for winter.", "price": 17},
    {"name": "Shorts", "description": "Casual shorts for hot weather.", "price": 23},
    {"name": "Belt", "description": "Leather belt for casual and formal wear.", "price": 13},
    
    {"name": "Coffee Maker", "description": "Automatic coffee maker with brew settings.", "price": 70},
    {"name": "Blender", "description": "High-speed blender for smoothies.", "price": 40},
    {"name": "Microwave", "description": "Compact microwave for quick cooking.", "price": 100},
    {"name": "Vacuum Cleaner", "description": "Powerful vacuum cleaner for all surfaces.", "price": 130},
    {"name": "Washing Machine", "description": "Energy-efficient washing machine with large capacity.", "price": 500},
    {"name": "Fridge", "description": "Double-door fridge with energy-saving features.", "price": 800},
    {"name": "Air Conditioner", "description": "Energy-efficient air conditioner.", "price": 350},
    {"name": "Dishwasher", "description": "Automatic dishwasher with multiple wash cycles.", "price": 500},
    {"name": "Toaster", "description": "Two-slice toaster with browning settings.", "price": 30},
    {"name": "Electric Kettle", "description": "Quick boiling electric kettle.", "price": 20},
    
    {"name": "Gaming Chair", "description": "Ergonomic gaming chair with adjustable armrests.", "price": 200},
    {"name": "Sofa", "description": "Comfortable sofa with a modern design.", "price": 500},
    {"name": "Coffee Table", "description": "Wooden coffee table with storage.", "price": 90},
    {"name": "Bookshelf", "description": "Four-tier bookshelf for storage.", "price": 120},
    {"name": "Dining Table", "description": "Wooden dining table for six people.", "price": 250},
    {"name": "Office Desk", "description": "Ergonomic office desk with drawers.", "price": 150},
    {"name": "Bed Frame", "description": "King-size bed frame with storage drawers.", "price": 300},
    {"name": "Wardrobe", "description": "Double-door wardrobe with multiple shelves.", "price": 350},
    {"name": "Nightstand", "description": "Compact nightstand with drawer storage.", "price": 60},
    {"name": "Bean Bag", "description": "Comfortable bean bag for relaxation.", "price": 40},
    
    {"name": "Fishing Rod", "description": "Lightweight fishing rod for casual anglers.", "price": 50},
    {"name": "Tennis Racket", "description": "Durable tennis racket for professional players.", "price": 90},
    {"name": "Soccer Ball", "description": "Official size soccer ball for matches.", "price": 30},
    {"name": "Yoga Mat", "description": "Non-slip yoga mat for practice.", "price": 20},
    {"name": "Dumbbells", "description": "Pair of adjustable dumbbells.", "price": 40},
    {"name": "Basketball", "description": "High-quality basketball for outdoor play.", "price": 25},
    {"name": "Golf Club", "description": "Premium golf club for beginners.", "price": 150},
    {"name": "Baseball Glove", "description": "Leather baseball glove for better grip.", "price": 60},
    {"name": "Running Shoes", "description": "Comfortable running shoes for all surfaces.", "price": 70},
    {"name": "Jump Rope", "description": "Durable jump rope for fitness training.", "price": 10},
    
    {"name": "Painting", "description": "Original canvas painting by a local artist.", "price": 250},
    {"name": "Sculpture", "description": "Handcrafted sculpture made from wood.", "price": 350},
    {"name": "Framed Print", "description": "Beautifully framed print of a landscape.", "price": 60},
    {"name": "Pottery", "description": "Handmade pottery with intricate designs.", "price": 80},
    {"name": "Wall Clock", "description": "Vintage-style wall clock with roman numerals.", "price": 40},
    {"name": "Vase", "description": "Decorative vase for home decor.", "price": 50},
    {"name": "Drawing Set", "description": "Complete drawing set for beginners.", "price": 30},
    {"name": "Canvas", "description": "High-quality canvas for painting.", "price": 15},
    {"name": "Easel", "description": "Wooden easel for painting and displaying artwork.", "price": 90},
    {"name": "Art Supplies", "description": "Essential supplies for all art projects.", "price": 20}
]


# Function to search products based on the query
def search_products(query):
    return [product for product in products if query.lower() in product["name"].lower()]

# Home route that renders chatbot.html
@app.route('/')
def home():
    return render_template('chatbot.html')  # Render chatbot.html

# Search endpoint
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    matching_products = search_products(query)
    return jsonify(matching_products)

if __name__ == '__main__':
    app.run(debug=True)
