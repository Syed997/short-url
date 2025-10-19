from flask import Flask
from app.blueprints.url.routes import url_bp

def create_app():
    app = Flask(__name__)


    app.register_blueprint(url_bp, url_prefix='/api')



    return app