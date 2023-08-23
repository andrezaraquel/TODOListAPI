from app import app
from flask import jsonify

@app.route("/users", methods=['GET'])
def get_users():
    return jsonify({'message': 'Users list'})