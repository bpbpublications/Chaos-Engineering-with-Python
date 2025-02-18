from flask import Flask, jsonify
import yaml, os

app = Flask(__name__)

@app.route('/')
def get_products():
    filename = 'products.yaml'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            products = yaml.safe_load(file)
        return jsonify(products)
    else:
        return "Product listing not found!", 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
