from app import app
from flask import jsonify
from ..views import users

@app.route("/users", methods=['GET'])
def get_users():
    return jsonify({'message': 'Users list'})

@app.route("/users", methods=['POST'])
def create_users():
    return users.create_user()