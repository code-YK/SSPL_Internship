from database.session import get_session
from models.city_data import CityWeather
from tabulate import tabulate

class ViewTable:
    @staticmethod
    def view_table():
        session = get_session()
        rows = session.query(CityWeather).all()

        table_data = [
            [row.city, row.region, row.country, row.temp_c, row.humidity, row.wind_kph, row.condition]
            for row in rows]

        headers = ["City", "Region", "Country", "Temp (°C)", "Humidity (%)", "Wind (kph)", "Condition"]

        print("\n--- Weather Data ---")
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        print("---------------------\n")

        session.close()