# config.py

import os

# OpenWeatherMap API key
API_KEY = os.getenv('OPENWEATHER_API_KEY', '273479e9a003f864778929ced8af11a1')

# Cities to monitor (major metros in India)
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Data retrieval interval (in minutes)
RETRIEVAL_INTERVAL = 5

# Alert thresholds (user configurable)
TEMP_THRESHOLD = 35  # Celsius


