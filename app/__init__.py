from flask import Flask
from .routes import weather_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(weather_bp)
    return app