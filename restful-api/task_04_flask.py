#!/usr/bin/env python3

from flask import request
from flask import jsonify
from flask import Flask
app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route pour la page d'accueil
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route pour servir les utilisateurs
@app.route('/data')
def get_data():
    # Retourne une liste de tous les noms d'utilisateurs
    return jsonify(list(users.keys()))

# Route pour vérifier le statut
@app.route('/status')
def status():
    return "OK"

# Route dynamique pour obtenir un utilisateur spécifique par son username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route pour ajouter un utilisateur via une requête POST
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()  # Récupère les données JSON envoyées dans la requête
    
    # Vérifie si un 'username' est fourni
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Ajoute l'utilisateur au dictionnaire
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
