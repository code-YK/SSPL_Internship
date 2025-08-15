import json
import logging

from api.clients import WeatherAPIClient
from api.schemas import WeatherData

from data_processing.get_user_input import get_city_input
from data_processing.insert_into_table import insert_data
from data_processing.view_table import ViewTable

from database.session import init_db


def cli_menu():
    
    API_KEY = "7d1b99af2de84eb78d7111257253107"
    client = WeatherAPIClient(API_KEY)

    while True:
        print("\n=== Weather CLI Menu ===")
        print("1. Enter city to fetch weather")
        print("2. View weather database")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            city = get_city_input()
            try:
                raw_data = client.fetch_weather(city)
                validated_data = WeatherData(**raw_data).dict()

                with open("weather_data.json", "a") as f:
                    json.dump(validated_data, f, indent=2)

                insert_data(validated_data)
                logging.info("Weather data inserted successfully.")

            except Exception as e:
                logging.error(f"Failed to fetch/insert data: {e}")

        elif choice == "2":
            ViewTable.view_table()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")