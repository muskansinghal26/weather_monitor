# thresholds.py

# Storage for thresholds (could be in-memory or database-driven)
alert_thresholds = {
    "temperature": None,  # Example: {"city": "Delhi", "threshold": 35, "duration": 2}
    "condition": None     # Example: {"city": "Mumbai", "condition": "Rain"}
}

def set_alert_thresholds(data):
    try:
        temperature_threshold = int(data.get('temperature_threshold', 0))  # Convert to integer
        humidity_threshold = int(data.get('humidity_threshold', 0))        # Convert to integer

        # Perform additional validations if needed
        if temperature_threshold < 0 or humidity_threshold < 0:
            raise ValueError("Thresholds must be non-negative numbers.")

        # Save or update the thresholds
        return {
            "message": "Threshold set successfully!",
            "temperature_threshold": temperature_threshold,
            "humidity_threshold": humidity_threshold
        }
    except ValueError as ve:
        raise ValueError(f"Invalid threshold type: {ve}")

def get_alert_thresholds():
    """
    Return the current alert thresholds.
    """
    return alert_thresholds

def check_alerts(weather_data):
    """
    Check if the latest weather data breaches any alert thresholds.
    
    weather_data: dict - Latest weather data (e.g., city, temperature, condition)
    """
    alerts = []

    # Check temperature threshold
    temp_threshold = alert_thresholds["temperature"]
    if temp_threshold and weather_data['city'] == temp_threshold['city']:
        if weather_data['temperature'] > temp_threshold['threshold']:
            alerts.append(f"Temperature alert in {weather_data['city']}: {weather_data['temperature']}°C exceeds {temp_threshold['threshold']}°C")

    # Check condition threshold
    condition_threshold = alert_thresholds["condition"]
    if condition_threshold and weather_data['city'] == condition_threshold['city']:
        if weather_data['condition'].lower() == condition_threshold['condition'].lower():
            alerts.append(f"Weather condition alert in {weather_data['city']}: {weather_data['condition']} detected")

    return alerts
