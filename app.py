# app.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Tes clés Enedis
API_PUBLIC_KEY = os.environ.get("ENEDIS_PUBLIC_KEY", "1JbIJjWokMTCIcFb7ZzOqX_EJaYa")
API_SECRET_KEY = os.environ.get("ENEDIS_SECRET_KEY", "1YGowjHfdhjSuqYvO9IeuMt5xIYa")

# Endpoint pour recevoir les callbacks d'Enedis
@app.route("/callback", methods=["POST"])
def callback():
    data = request.json
    print("Données reçues de Enedis :", data)
    return jsonify({"status": "ok"}), 200

# Exemple pour faire une requête à l'API Enedis
@app.route("/get_data", methods=["GET"])
def get_data():
    endpoint = "https://enedis.fr/api/endpoint"  # Remplace par l'endpoint réel
    headers = {
        "Authorization": f"Bearer {API_PUBLIC_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "some_parameter": "value",
        "callback_url": "https://ton-domaine.com/callback"
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "key.pem"))
