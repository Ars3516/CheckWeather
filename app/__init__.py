from flask import Flask
from app.config import Config
from app.controllers.weather_controller import weather_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(weather_blueprint)

    return app