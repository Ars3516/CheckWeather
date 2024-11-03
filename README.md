# Flask Weather API

## Project Description

Flask Weather API is a RESTful web service built using Flask that provides current weather data and 7-day weather forecasts from the Weatherbit API. This application allows users to fetch weather information by city name or geographical coordinates. It supports API versioning and implements structured error handling to ensure smooth interactions with clients.

## API Endpoints

### Current Weather

- **GET `/api/v1/weather/cities/<city>`**
  - Retrieve the current weather for the specified city.
  - **Path Parameters**:
    - `city`: The name of the city for which to retrieve weather information.
  
### Current Weather by Coordinates

- **GET `/api/v1/weather/coordinates/<float:lat>/<float:lon>`**
  - Retrieve the current weather for the specified geographical coordinates.
  - **Path Parameters**:
    - `lat`: Latitude of the location.
    - `lon`: Longitude of the location.

### 7-Day Weather Forecast

- **GET `/api/v1/weather/forecast/cities/<city>`**
  - Retrieve a 7-day weather forecast for the specified city.
  - **Path Parameters**:
    - `city`: The name of the city for which to retrieve the forecast.


