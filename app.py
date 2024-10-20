from flask import Flask, jsonify, request
from weather_service import monitor_weather, get_daily_summary, get_weather_forecast
from thresholds import check_alerts, get_alert_thresholds, set_alert_thresholds
from apscheduler.schedulers.background import BackgroundScheduler
import time

app = Flask(__name__)

scheduler = BackgroundScheduler()

# Function to fetch weather data and check alerts
def check_alerts_job():
    # Fetch the latest weather data
    weather_data = monitor_weather()  # Ensure this function returns the necessary data
    alerts = check_alerts(weather_data)  # Call check_alerts with the retrieved weather_data

    # Log or print alerts if any
    if alerts:
        for alert in alerts:
            print(alert)

# Schedule the job to run every 10 minutes
scheduler.add_job(check_alerts_job, 'interval', minutes=10)

scheduler.start()

@app.route('/set_threshold', methods=['POST'])
def set_threshold():
    """Endpoint to set alert thresholds for temperature or weather conditions."""
    data = request.get_json()
    threshold_type = data.get('type')
    city = data.get('city')
    threshold_value = data.get('value')
    duration = data.get('duration', 1)  # Default duration is 1 if not provided

    set_alert_thresholds(threshold_type, city, threshold_value, duration)
    return jsonify({"message": "Threshold set successfully", "thresholds": get_alert_thresholds()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

    # Keeping the script running
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
