from flask import Blueprint, request, jsonify
from .services import get_weather_data, get_forecast_data

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather/city', methods=['GET'])
def get_weather_by_city():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required."}), 400
    return get_weather_data(city=city)

@weather_bp.route('/weather/coordinates', methods=['GET'])
def get_weather_by_coordinates():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({"error": "Latitude and longitude parameters are required."}), 400
    return get_weather_data(lat=lat, lon=lon)

@weather_bp.route('/weather/forecast', methods=['GET'])
def get_forecast_by_city():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required."}), 400
    return get_forecast_data(city)
