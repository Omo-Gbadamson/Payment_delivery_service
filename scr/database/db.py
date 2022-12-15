from flask_mongoengine import MongoEngine

from pymongo import monitoring

from scr.utility.log import CommandLogger

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
import app


db = SQLAlchemy(app)

def initialize_db(app):
    db.init_app(app)

monitoring.register(CommandLogger())
