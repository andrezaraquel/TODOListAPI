from werkzeug.security import generate_password_hash
from app import db
from flask import request
from ..models.users import Users, user_schema

def create_user():
    try:
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']

        pass_hash = generate_password_hash(password)

        user = Users(username, pass_hash, name)

        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except:
        return None

def get_user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None