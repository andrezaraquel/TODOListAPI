from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config.from_mapping(Config.config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    db.create_all()

from .routes import routes
from .models import users
