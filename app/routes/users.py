from app import app
from flask import jsonify

from . import auth
from ..views import users

@app.route("/users/auth", methods=['GET'])
@auth.token_required
def hello(current_user):
    return jsonify({'message': 'user authentiated', 'data': {'username': current_user.username}}), 200

@app.route("/users", methods=['POST'])
def create_users():
    user = users.create_user()
    if user:
        return jsonify({'message': 'successfully registered', 'result': user}), 201
    return jsonify({'message': 'unable to create', 'data': {}}), 400

@app.route('/login', methods=['POST'])
def authenticate():
    return auth.auth()