import requests
from app.config import Config
from .exceptions import CityNotFoundError, ExternalAPIError

def get_weather_data(city):
    url = f"{Config.WEATHERBIT_BASE_URL}/current?city={city}&key={Config.WEATHERBIT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 404:
        raise CityNotFoundError(f"City '{city}' not found.")
    elif response.status_code != 200:
        raise ExternalAPIError("Error occurred while fetching data from Weatherbit API")

    data = response.json()
    return {
        "city": data['data'][0]['city_name'],
        "temperature": data['data'][0]['temp'],
        "weather": data['data'][0]['weather']['description'],
        "humidity": data['data'][0]['rh'],
        "wind_speed": data['data'][0]['wind_spd'],
        "wind_direction": data['data'][0]['wind_cdir'],
        "date": data['data'][0]['datetime']
    }
def get_weather_by_coordinates(lat, lon):
    url = f"{Config.WEATHERBIT_BASE_URL}/current?lat={lat}&lon={lon}&key={Config.WEATHERBIT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 404:
        raise CityNotFoundError("Coordinates not found.")
    elif response.status_code != 200:
        raise ExternalAPIError("Error occurred while fetching data from Weatherbit API")

    data = response.json()
    return {
        "city": data['data'][0]['city_name'],
        "latitude": data['data'][0]['lat'],
        "longitude": data['data'][0]['lon'],
        "temperature": data['data'][0]['temp'],
        "weather": data['data'][0]['weather']['description'],
        "humidity": data['data'][0]['rh'],
        "wind_speed": data['data'][0]['wind_spd'],
        "wind_direction": data['data'][0]['wind_cdir'],
        "date": data['data'][0]['datetime']
    }

def get_forecast_by_city(city):
    url = f"{Config.WEATHERBIT_BASE_URL}/forecast/daily?city={city}&key={Config.WEATHERBIT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 404:
        raise CityNotFoundError(f"City '{city}' not found.")
    elif response.status_code != 200:
        raise ExternalAPIError("Error occurred while fetching forecast data from Weatherbit API")

    data = response.json()
    return {
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
