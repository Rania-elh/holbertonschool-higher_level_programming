#!/usr/bin/env python3
"""
Flask application with dynamic content rendering using Jinja.
"""

import json
from flask import Flask, render_template

app = Flask(__name__)

def load_items():
    """Load items from JSON file."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            return data.get('items', [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@app.route('/')
def home():
    """Route for the home page."""
    return render_template('index.html')

@app.route('/items')
def items():
    """Route for displaying items list."""
    items_list = load_items()
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
