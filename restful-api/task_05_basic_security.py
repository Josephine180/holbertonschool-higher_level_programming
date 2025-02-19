#!/usr/bin/env python3
from flask import request, jsonify, Flask
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, 
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Setup JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt_manager = JWTManager(app)

# Setup Basic Auth
auth = HTTPBasicAuth()

# Users database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic auth verification
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

# Routes
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]}
        )
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})

# JWT error handlers
@jwt_manager.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt_manager.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt_manager.expired_token_loader
def handle_expired_token_error(header, payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt_manager.revoked_token_loader
def handle_revoked_token_error(header, payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt_manager.needs_fresh_token_loader
def handle_needs_fresh_token_error(header, payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)