from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    products = [
    {
    'name': 'Product 1',
    'price': 10.0
    },
    {
    'name': 'Product 2',
    'price': 20.0
    },
    {
    'name': 'Product 3',
    'price': 30.0
    }
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
