from flask import jsonify

def successful_creation(message, result):
    return jsonify({'message': message, 'data': result}), 201

def successful_operation(message, result):
    return jsonify({'message': message, 'data': result}), 200

def unsuccessful_operation(message, error):
    return jsonify({'message': message, 'data': error}), 401

def add_task_bad_request():
    return jsonify({'message': 'the request body must contain "title", "description" and "status"', 'data': ""}), 401