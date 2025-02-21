from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify({"you_sent": data}), 201

@app.route('/api/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    return jsonify({"message": f"Item {item_id} updated with data: {data}"}), 200

@app.route('/api/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify({"message": f"Item {item_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

