from data_collector import DataCollector

cities = [
    "Almaty",
    "Moscow",
    "London"
]

for city in cities:
    print(f"Getting temperature data for {city}.")
    print(f"Temperature from weatherapi.com: {DataCollector().collect_weather_data(city=city)}")
    print(f"Temperature from weatherapi.com: {DataCollector().collect_open_weather_data(city=city)}")
