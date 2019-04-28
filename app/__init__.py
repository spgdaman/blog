# app's __init__.py file
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    db.init_app(app)

    # registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app