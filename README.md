# Real-Time Weather Monitoring System with Rollups and Aggregates

## Overview
This application is designed to monitor weather conditions in real-time using data from the OpenWeatherMap API. It provides features such as temperature rollups, weather condition summaries, and user-configurable alert thresholds. The system supports real-time data collection for multiple cities and allows users to view historical data and forecasts.

## Key Features:

-Real-time weather data monitoring: Continuously retrieve data from OpenWeatherMap at user-configured intervals.

-Rollups and aggregates: Calculate daily weather summaries including average, max, min temperatures, and dominant weather conditions.

-Alerting system: User-defined thresholds trigger alerts when conditions are met (e.g., temperature exceeding 35°C).

-Forecast integration: Retrieve weather forecasts for future conditions and generate summaries.

-Visualization: Provide graphs and charts for daily summaries, trends, and alerts (using libraries such as Matplotlib).

## Design Choices

### Architecture

- ***Flask Framework***: This Python micro-framework is used to handle API routes, user requests, and scheduling of weather data retrieval.
  
-***APSchedule***r: The task scheduling library handles periodic weather data retrieval and threshold checking.

-***PostgreSQL***: Weather data and daily summaries are stored in a PostgreSQL database for persistence.

-***OpenWeatherMap API***: External weather data is fetched using this API. Both real-time and forecast data are integrated into the system.

-***Visualization***: Weather data trends and summaries are visualized using Matplotlib for interactive and static graph generation.

## Data Model

-***Weather Data***: Stores raw weather data retrieved from the API.

-***Daily Summary***: Aggregates data including min, max, average temperatures, and dominant weather condition for each city.

-***Alerts***: Stores and tracks user-defined alert conditions and thresholds for each city.

## Error Handling

-***API Key Errors***: Handles invalid or expired API keys by logging errors and notifying the user.

-***Threshold Handling***: Validates threshold values and types before storing them in the system to avoid runtime errors.

## Build Instructions

**Prerequisites**

Ensure you have the following installed on your system:

1.Python 3.x (preferably Python 3.9 or higher)
2.PostgreSQL 13+
3.OpenWeatherMap API Key (sign up at OpenWeatherMap)

## Step-by-Step Setup

1. Clone the repository
   
git clone https://github.com/muskansinghal26/weather_monitor.git
cd weather_monitor

2. Set up a virtual environment
   
It is recommended to use a virtual environment to manage dependencies:

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

3. Install dependencies
   
Install the required dependencies listed in requirements.txt
pip install -r requirements.txt

**Dependencies include:**

-Flask
-APScheduler
-Requests
-Psycopg2 (PostgreSQL adapter)
-Matplotlib (for visualization)

4. Set up PostgreSQL database
1.Ensure PostgreSQL is running.

2.Create a new database:
psql -U postgres
CREATE DATABASE weather_monitor;

3.Update the database credentials in config.py:
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/weather_monitor'

4. Configure environment variables
You need to set up environment variables for:

OPENWEATHER_API_KEY: Your OpenWeatherMap API Key.
***Example (Linux/MacOS):***

export OPENWEATHER_API_KEY='your_api_key'

***Example (Windows Command Prompt):***

set OPENWEATHER_API_KEY=your_api_key

6. Initialize the database
To create the required tables, run the following:

python init_db.py

7. Run the application
Start the Flask development server:

python app.py
The application should now be accessible at http://127.0.0.1:5000.

8. Testing
To run tests:

python -m unittest discover

## API Endpoints
1. **POST /set_threshold**

- Allows users to set alert thresholds for temperature and other weather conditions.
- Example body:
  {
  "threshold_type": "temperature",
  "city": "Mumbai",
  "threshold_value": 35,
  "duration": 2
}

2. **GET /get_summary**

Retrieves the daily weather summary for all cities.

3.**GET /get_forecast**

Fetches and displays forecast data.

## Running with Docker

To containerize the application, follow these steps:

1. Build the Docker image:
   
docker build -t weather_monitor .

2. Run the container:

docker run -d -p 5000:5000 --env OPENWEATHER_API_KEY=your_api_key weather_monitor

## Troubleshooting

- **Connection Refused on localhost:** Ensure the Flask server is running and accessible at http://127.0.0.1:5000.
  
-**API Key Error:** Ensure that the OpenWeatherMap API key is set up as an environment variable and valid.
  
-**Database Connection Issues:** Check PostgreSQL service status and ensure credentials in config.py are correct.

## Future Improvements

-Add support for additional weather parameters like wind speed, humidity, and air pressure in rollups and aggregates.

-Enhance the alerting system to send notifications via email/SMS.

-Add forecast-based alerting to predict future threshold breaches.


This README provides everything you need to build, configure, and run the weather monitoring system. Let me know if you need further adjustments or clarifications!
