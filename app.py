# app.py
from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

# Clés Enedis chargées depuis les variables d'environnement
API_PUBLIC_KEY = os.environ.get("ENEDIS_PUBLIC_KEY")
API_SECRET_KEY = os.environ.get("ENEDIS_SECRET_KEY")

# Vérification que les clés sont bien définies
if not API_PUBLIC_KEY or not API_SECRET_KEY:
    raise ValueError("Les clés ENEDIS_PUBLIC_KEY et ENEDIS_SECRET_KEY doivent être définies dans les variables d'environnement")

# Page d'accueil de l'API
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API ENEDIS - Serveur HTTPS",
        "version": "1.0",
        "endpoints": {
            "/": "Page d'accueil (GET)",
            "/callback": "Endpoint pour recevoir les callbacks d'Enedis (POST)",
            "/get_data": "Exemple de requête à l'API Enedis (GET)"
        },
        "status": "running"
    })

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
