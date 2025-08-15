from sqlalchemy import Column, String, Float
from models.base import Base

class CityWeather(Base):
    __tablename__ = 'city_weather'

    city = Column(String, primary_key=True)
    region = Column(String)
    country = Column(String)
    temp_c = Column(Float)
    humidity = Column(Float)
    wind_kph = Column(Float)
    condition = Column(String)
