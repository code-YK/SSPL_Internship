from models.city_data import CityWeather
from database.session import get_session

def insert_data(data):
    session = get_session()

    city_weather = CityWeather(
        city=data["location"]["name"],
        region=data["location"]["region"],
        country=data["location"]["country"],
        temp_c=data["current"]["temp_c"],
        humidity=data["current"]["humidity"],
        wind_kph=data["current"]["wind_kph"],
        condition=data["current"]["condition"]["text"]
    )

    session.merge(city_weather)
    session.commit()
    session.close()

