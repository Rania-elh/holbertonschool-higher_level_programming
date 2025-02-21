import requests

def send_get_request():
    url = "http://127.0.0.1:5000/api/hello"  # URL de l'API Flask
    response = requests.get(url)
    if response.status_code == 200:
        print("GET request success:", response.json())  # Affiche la réponse JSON du serveur
    else:
        print(f"GET request failed with status code {response.status_code}")

def send_post_request():
    url = "http://127.0.0.1:5000/api/data"
    data = {"name": "Alice", "age": 25}  # Exemple de données envoyées
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("POST request success:", response.json())
    else:
        print(f"POST request failed with status code {response.status_code}")

if __name__ == '__main__':
    send_get_request()
    send_post_request()

