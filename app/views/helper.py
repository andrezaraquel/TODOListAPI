from werkzeug.security import check_password_hash
from app.views.users import get_user_by_username
from flask import request, jsonify
from app import app
import jwt
import datetime

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    
    user = get_user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 401
    
    if user and check_password_hash(user.password, auth.password):
        expiration = datetime.datetime.now() + datetime.timedelta(hours=12)
        token = jwt.encode({'username': user.username, 'exp': expiration}, app.config['SECRET_KEY'])
        return jsonify({'message': 'validated successfully', 'exp': expiration, 'token': token}), 200
    
    else:
        return jsonify({'message': 'incorrect password', 'data': {}}), 401