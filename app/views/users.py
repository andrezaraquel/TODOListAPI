from flask import jsonify

def successfully_registered(user):
    return jsonify({'message': 'successfully registered', 'result': user}), 201

def unable_to_create_user(result):
    return jsonify({'message': 'unable to create', 'data': result}), 400

def successfully_validated(expiration, token):
    return jsonify({'message': 'successfully validated', 'exp': expiration, 'token': token}), 200

def validation_failed(message):
    return jsonify({'message': message, 'data': {}}), 401