from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)
API_GATEWAY_URL = 'http://localhost:8000'

@app.route('/products')
def get_products():
    response = requests.get(API_GATEWAY_URL)
    if response.status_code == 200:
        products = response.json()
        return jsonify(products)
    else:
        abort(500, 'Product listing not found!')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
