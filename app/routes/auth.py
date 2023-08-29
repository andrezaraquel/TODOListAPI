from functools import wraps
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
        token = jwt.encode({'username': user.username, 'exp': expiration}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'message': 'validated successfully', 'exp': expiration, 'token': token}), 200
    return jsonify({'message': 'incorrect password', 'data': {}}), 401
    
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = get_user_by_username(data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired'}), 401
        return func(current_user, *args, **kwargs)

    return decorated