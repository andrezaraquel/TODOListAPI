from werkzeug.security import generate_password_hash
from app import app
from flask import jsonify, request

from . import auth
from ..models.users import Users
from ..views.users import *

@app.route("/users/auth", methods=['GET'])
@auth.token_required
def hello(current_user):
    return jsonify({'message': 'user authentiated', 'data': {'username': current_user.username}}), 200

@app.route("/users", methods=['POST'])
def create_users():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    pass_hash = generate_password_hash(password)
    result = Users.create_user(username, pass_hash, name)
    if isinstance(result, dict):
        return successfully_registered(result)
    return unable_to_create_user(result)

@app.route('/login', methods=['POST'])
def authenticate():
    return auth.auth()