from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_mapping(Config.config)

from .routes import routes

db = SQLAlchemy().init_app(app)