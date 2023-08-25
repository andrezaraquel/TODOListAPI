from app import app
from flask import jsonify
from ..views import users, helper

@app.route("/users/auth", methods=['GET'])
@helper.token_required
def hello(current_user):
    return jsonify({'message': 'user authentiated', 'data': {'username': current_user.username}}), 200

@app.route("/users", methods=['POST'])
def create_users():
    return users.create_user()

@app.route('/login', methods=['POST'])
def authenticate():
    return helper.auth()