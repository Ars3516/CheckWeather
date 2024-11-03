from flask import Blueprint, request, jsonify
from app.services.weather_service import get_weather_data, get_weather_by_coordinates, get_forecast_by_city
from app.services.exceptions import CityNotFoundError, ExternalAPIError

weather_blueprint = Blueprint("weather", __name__, url_prefix="/api/v1/")


@weather_blueprint.route('weather/cities/<string:city>', methods=['GET'])
def get_weather(city):
    try:
        weather_data = get_weather_data(city)
        return jsonify(weather_data), 200
    except CityNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ExternalAPIError:
        return jsonify({"error": "An external service error occurred. Please try again later."}), 503



@weather_blueprint.route('weather/coordinates', methods=['GET'])
def get_by_coordinates():
    request_data = request.get_json()

    lat = request_data['lat']
    lon = request_data['lon']

    try:
        weather_data = get_weather_by_coordinates(lat, lon)
        return jsonify(weather_data), 200
    except ExternalAPIError:
        return jsonify({"error": "An external service error occurred. Please try again later."}), 503
    except Exception:
        return jsonify({"error": "An internal server error occurred."}), 500


@weather_blueprint.route('weather/forecast/cities/<string:city>', methods=['GET'])
def get_forecast(city):
    try:
        forecast_data = get_forecast_by_city(city)
        return jsonify(forecast_data), 200
    except CityNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ExternalAPIError:
        return jsonify({"error": "An external service error occurred. Please try again later."}), 503
    except Exception:
        return jsonify({"error": "An internal server error occurred."}), 500
