#!/usr/bin/env python3

from flask import request
from flask import jsonify
from flask import Flask
app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def user():
    return jsonify(users)

@app.route('/status')
def get_status():
    return({"message":"OK"}), 200

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')

    if username:
        users[username] = data  # Ajoute l'utilisateur
        return jsonify({"message": f"Utilisateur {username} ajouté avec succès !", "user": data}), 201
    else:
        return jsonify({"error": "Le 'username' est requis."}), 400


if __name__ == "__main__":
    app.run(debug=True)
