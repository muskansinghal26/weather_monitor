# db_setup.py

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# SQLite database setup
Base = declarative_base()
engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)
session = Session()

# Weather summary model
class WeatherSummary(Base):
    __tablename__ = 'weather_summaries'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    date = Column(Date)
    avg_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    dominant_condition = Column(String)

# Alert model
class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    condition = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)
