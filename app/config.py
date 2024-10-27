import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WEATHERBIT_API_KEY = os.getenv("WEATHERBIT_API_KEY")
    WEATHERBIT_BASE_URL = "https://api.weatherbit.io/v2.0"
