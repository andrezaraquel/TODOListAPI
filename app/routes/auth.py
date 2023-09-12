from functools import wraps
from werkzeug.security import check_password_hash
from app.models.users import Users
from app.views.users import *
from flask import request
from app import app
import jwt
import datetime

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return validation_failed('login required')

    user = Users.get_user_by_username(auth.username)
    if not user:
        return validation_failed('user not found')

    if user and check_password_hash(user.password, auth.password):
        expiration = datetime.datetime.now() + datetime.timedelta(hours=12)
        token = jwt.encode({'username': user.username, 'exp': expiration}, app.config['SECRET_KEY'], algorithm='HS256')
        return successfully_validated(expiration, token)
    return validation_failed('incorrect password')

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return validation_failed('token is missing')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = Users.get_user_by_username(data['username'])
        except:
            return validation_failed('token is invalid or expired')
        return func(current_user, *args, **kwargs)

    return decorated