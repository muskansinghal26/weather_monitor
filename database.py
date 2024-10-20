# database.py

# Sample in-memory storage (replace with actual DB fetch if needed)
weather_storage = []

def store_weather_data(data):
    """Stores weather data (add your actual DB logic here)."""
    weather_storage.append(data)

def fetch_daily_weather_data():
    """Fetch weather data for the day (replace with actual DB fetch)."""
    return weather_storage
