from app import app
from flask import jsonify
from ..views import users, helper

@app.route("/users", methods=['POST'])
def create_users():
    return users.create_user()

@app.route('/auth', methods=['POST'])
def authenticate():
    return helper.auth()