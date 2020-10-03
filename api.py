import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/products/laptops')
def get_products():
    with open('out/out.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def hi():
    return {"message": "Welcome to API Products"}