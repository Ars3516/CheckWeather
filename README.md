Dependencies
1.Flask - Web framework for building the API
2/requests - For making HTTP requests to the Weatherbit API
3.python-dotenv - For managing environment variables

This Flask application serves as a weather data API, leveraging the Weatherbit API to provide current weather and 7-day forecast data. It has three main endpoints to fetch weather information by city name or geographic coordinates.

Features
1.Current Weather by City: Retrieves the current weather data for a specified city.
2.Current Weather by Coordinates: Retrieves the current weather data using latitude and longitude coordinates.
3.7-Day Forecast by City: Provides a 7-day forecast for a specified city.

API Endpoints
1. Get Current Weather by City
Endpoint: /weather/city
Method: GET
Parameters:
city (required): Name of the city.

Get Current Weather by Coordinates
Endpoint: /weather/coordinates
Method: GET
Parameters:
lat (required): Latitude of the location.
lon (required): Longitude of the location.

Get 7-Day Forecast by City
Endpoint: /weather/forecast
Method: GET
Parameters:
city (required): Name of the city.
