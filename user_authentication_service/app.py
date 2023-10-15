#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort
from auth import Auth
import crypt
from db import DB
app = Flask(__name__)
AUTH = Auth()
db = DB()

@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """register user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Log in"""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
