import requests
from flask import jsonify
from .config import Config


def get_weather_data(city=None, lat=None, lon=None):
    if city:
        url = f"{Config.WEATHERBIT_BASE_URL}/current?city={city}&key={Config.WEATHERBIT_API_KEY}"
    else:
        url = f"{Config.WEATHERBIT_BASE_URL}/current?lat={lat}&lon={lon}&key={Config.WEATHERBIT_API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "location": data['data'][0].get('city_name', 'N/A'),
            "temperature": data['data'][0]['temp'],
            "weather": data['data'][0]['weather']['description'],
            "humidity": data['data'][0]['rh'],
            "wind_speed": data['data'][0]['wind_spd'],
            "wind_direction": data['data'][0]['wind_cdir'],
            "date": data['data'][0]['datetime']
        })
    return jsonify({"error": "Location not found."}), response.status_code

def get_forecast_data(city):
    url = f"{Config.WEATHERBIT_BASE_URL}/forecast/daily?city={city}&key={Config.WEATHERBIT_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "city": data['city_name'],
            "forecast": [
                {
                    "date": day['datetime'],
                    "temperature": day['temp'],
                    "weather": day['weather']['description']
                } for day in data['data']
            ]
        })
    return jsonify({"error": "City not found."}), response.status_code
