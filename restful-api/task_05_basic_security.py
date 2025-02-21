from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Fonction de sécurité de base (vérification d'un token)
def check_authentication():
    token = request.headers.get('Authorization')
    if not token or token != "Bearer my_secure_token":
        abort(403, description="Forbidden: Invalid token")

@app.route('/api/secure_data', methods=['GET'])
def get_secure_data():
    check_authentication()  # Vérification du token avant de traiter la requête
    return jsonify({"message": "This is secure data!"})

if __name__ == '__main__':
    app.run(debug=True)

