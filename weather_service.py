# weather_service.py

import requests
import time
from config import API_KEY, CITIES, RETRIEVAL_INTERVAL
from db_setup import session, WeatherSummary
from sqlalchemy import func
import datetime
from database import fetch_daily_weather_data

def get_weather_forecast(city):
    """Fetch weather forecast data from OpenWeatherMap API for a city."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        forecast_data = response.json()

        # Extract relevant forecast data (e.g., temp, condition, time)
        forecast_summary = []
        for forecast in forecast_data['list']:
            entry = {
                "timestamp": forecast['dt_txt'],
                "temperature": forecast['main']['temp'],
                "feels_like": forecast['main']['feels_like'],
                "condition": forecast['weather'][0]['description']
            }
            forecast_summary.append(entry)

        return forecast_summary
    
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_daily_summary():
    """Fetch and calculate the daily weather summary."""
    # Fetch weather data from the database (or wherever it's stored)
    weather_data = fetch_daily_weather_data()

    if not weather_data:
        return {"message": "No weather data available"}

    # Initialize variables to store aggregates
    total_temp = 0
    total_humidity = 0
    total_wind_speed = 0
    count = len(weather_data)
    
    min_temp = float('inf')
    max_temp = float('-inf')
    weather_condition_counts = {}

    # Aggregate data
    for entry in weather_data:
        total_temp += entry['temperature']
        total_humidity += entry['humidity']
        total_wind_speed += entry['wind_speed']

        if entry['temperature'] < min_temp:
            min_temp = entry['temperature']
        if entry['temperature'] > max_temp:
            max_temp = entry['temperature']

        # Count weather conditions to find the dominant one
        condition = entry['condition']
        if condition in weather_condition_counts:
            weather_condition_counts[condition] += 1
        else:
            weather_condition_counts[condition] = 1

    # Calculate averages
    avg_temp = total_temp / count
    avg_humidity = total_humidity / count
    avg_wind_speed = total_wind_speed / count

    # Find the dominant weather condition
    dominant_condition = max(weather_condition_counts, key=weather_condition_counts.get)

    # Return the daily summary
    daily_summary = {
        "average_temperature": avg_temp,
        "min_temperature": min_temp,
        "max_temperature": max_temp,
        "average_humidity": avg_humidity,
        "average_wind_speed": avg_wind_speed,
        "dominant_condition": dominant_condition
    }
    
    return daily_summary


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def process_weather_data(data, city):
    main = data['weather'][0]['main']
    temp = kelvin_to_celsius(data['main']['temp'])
    feels_like = kelvin_to_celsius(data['main']['feels_like'])
    dt = datetime.datetime.fromtimestamp(data['dt'])

    # Check if a summary for today already exists
    today = datetime.date.today()
    existing_summary = session.query(WeatherSummary).filter_by(city=city, date=today).first()

    if not existing_summary:
        # Create a new summary if it doesn't exist
        new_summary = WeatherSummary(
            city=city, date=today, avg_temp=temp, max_temp=temp, min_temp=temp, dominant_condition=main
        )
        session.add(new_summary)
    else:
        # Update the existing summary
        existing_summary.avg_temp = (existing_summary.avg_temp + temp) / 2
        existing_summary.max_temp = max(existing_summary.max_temp, temp)
        existing_summary.min_temp = min(existing_summary.min_temp, temp)
        existing_summary.dominant_condition = main  # For simplicity, updating with the latest condition

    session.commit()

def monitor_weather():
    # Replace with your actual API call to OpenWeatherMap
    api_key = "273479e9a003f864778929ced8af11a1"
    city = "Delhi"  # You can extend this to handle multiple cities
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    # Extract relevant data
    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],  # Temperature in Celsius
        "condition": data["weather"][0]["description"],  # Weather condition
    }

    return weather_data
