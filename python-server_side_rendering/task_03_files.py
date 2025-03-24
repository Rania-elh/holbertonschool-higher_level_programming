from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    """Reads products from the JSON file."""
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv_file():
    """Reads products from the CSV file."""
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

@app.route('/products')
def products():
    # Get the query parameters for source and id
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)  # id is optional

    if source not in ['json', 'csv']:
        error_message = "Wrong source. Please use 'json' or 'csv'."
        return render_template('product_display.html', error=error_message)

    # Read the data based on the source
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()

    # If id is provided, filter the products
    if product_id:
        products = [product for product in products if product['id'] == product_id]

    # If no products found with the id, show error
    if product_id and not products:
        error_message = "Product not found."
        return render_template('product_display.html', error=error_message)

    # Render the template with products data
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
