from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

#
# load_dotenv()
# WEATHERBIT_API_KEY = os.getenv("WEATHERBIT_API_KEY")
#
#
# def get_weather_by_city(city):
#     url = f'http://api.weatherbit.io/v2.0/current?city={city}&key={WEATHERBIT_API_KEY}'
#     response = requests.get(url)
#     return response.json()
#
#
# app = Flask(__name__)
#
# WEATHERBIT_BASE_URL = "https://api.weatherbit.io/v2.0"
#
#
# @app.route('/weather/city', methods=['GET'])
# def get_weather_by_city():
#     city = request.args.get('city')
#     if not city:
#         return jsonify({"error": "City parameter is required."}), 400
#
#

# load_dotenv()
# WEATHERBIT_API_KEY = os.getenv("WEATHERBIT_API_KEY")
#
# app = Flask(__name__)
#
# WEATHERBIT_BASE_URL = "https://api.weatherbit.io/v2.0"
# # WEATHERBIT_BASE_URL = "https://www.weatherbit.io/api/weather-current"
#
# @app.route('/weather/city', methods=['GET'])
# def get_weather_by_city():
#     city = request.args.get('city')
#     if not city:
#         return jsonify({"error": "City parameter is required."}), 400
#
#     url = f"{WEATHERBIT_BASE_URL}/current?city={city}&key={WEATHERBIT_API_KEY}"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         weather_data = {
#             "city": data['data']['city_name'],
#             "temperature": data['data']['temp'],
#             "weather": data['data']['weather']['description'],
#             "humidity": data['data']['rh'],
#             "wind_speed": data['data']['wind_spd'],
#             "wind_direction": data['data']['wind_cdir'],
#             "date": data['data']['datetime']
#         }
#         return jsonify(weather_data)
#     else:
#         return jsonify({"error": "City not found."}), 404
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
WEATHERBIT_API_KEY = os.getenv("WEATHERBIT_API_KEY")

app = Flask(__name__)

WEATHERBIT_BASE_URL = "https://api.weatherbit.io/v2.0"


@app.route('/weather/city', methods=['GET'])
def get_weather_by_city():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required."}), 400

    url = f"{WEATHERBIT_BASE_URL}/current?city={city}&key={WEATHERBIT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data['data'][0]['city_name'],
            "temperature": data['data'][0]['temp'],
            "weather": data['data'][0]['weather']['description'],
            "humidity": data['data'][0]['rh'],
            "wind_speed": data['data'][0]['wind_spd'],
            "wind_direction": data['data'][0]['wind_cdir'],
            "date": data['data'][0]['datetime']
        }
        return jsonify(weather_data)
    else:
        return jsonify({"error": "City not found."}), 404


@app.route('/weather/coordinates', methods=['GET'])
def get_weather_by_coordinates():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Latitude and longitude parameters are required."}), 400

    url = f"{WEATHERBIT_BASE_URL}/current?lat={lat}&lon={lon}&key={WEATHERBIT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "latitude": data['data'][0]['lat'],
            "longitude": data['data'][0]['lon'],
            "temperature": data['data'][0]['temp'],
            "weather": data['data'][0]['weather']['description'],
            "humidity": data['data'][0]['rh'],
            "wind_speed": data['data'][0]['wind_spd'],
            "wind_direction": data['data'][0]['wind_cdir'],
            "date": data['data'][0]['datetime']
        }
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Invalid coordinates."}), 404


@app.route('/weather/forecast', methods=['GET'])
def get_forecast_by_city():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required."}), 400

    url = f"{WEATHERBIT_BASE_URL}/forecast/daily?city={city}&key={WEATHERBIT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast_data = {
            "city": data['city_name'],
            "forecast": [
                {
                    "date": day['datetime'],
                    "temperature": day['temp'],
                    "weather": day['weather']['description']
                }
                for day in data['data']
            ]
        }
        return jsonify(forecast_data)
    else:
        return jsonify({"error": "City not found."}), 404


if __name__ == '__main__':
    app.run(debug=False)