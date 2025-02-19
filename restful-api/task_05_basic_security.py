#!/usr/bin/env python3

from flask import request
from flask import jsonify
from flask import Flask
import jwt
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

@app.route('/login', methods =['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    user = users.get(username)
    if user and check_password_hash(user["password"],password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    print(f"User identity: {current_user}") 
    return jsonify({"message": "JWT Auth: Access Granted", "logged_in_as": current_user}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})

# Custom error handlers for JWT errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)