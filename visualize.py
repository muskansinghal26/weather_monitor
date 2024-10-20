# visualize.py

import matplotlib.pyplot as plt
from db_setup import session, WeatherSummary
import datetime

def visualize_daily_summary():
    today = datetime.date.today()

    cities = session.query(WeatherSummary.city).distinct().all()
    for city in cities:
        summaries = session.query(WeatherSummary).filter_by(city=city[0], date=today).all()
        
        dates = [s.date for s in summaries]
        temps = [s.avg_temp for s in summaries]

        plt.plot(dates, temps, label=city[0])

    plt.xlabel('Date')
    plt.ylabel('Avg Temperature (°C)')
    plt.title('Daily Weather Summary')
    plt.legend()
    plt.show()
