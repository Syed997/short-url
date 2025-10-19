from flask import Flask
from app.blueprints.url.routes import url_bp
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(url_bp, url_prefix='/api')



    return app