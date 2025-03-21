import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int) 


    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    
    if source == 'json':
        products = read_json_file('products.json')
    else:
        products = read_csv_file('products.csv')


    if product_id:
        products = [product for product in products if product['id'] == product_id]

    
    if product_id and not products:
        return render_template('product_display.html', error="Product not found")

   
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
