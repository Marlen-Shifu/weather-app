from open_weather_api_service import OpenWeatherAPIService
from weather_api_service import WeatherAPIService


class DataCollector:

    weather_service = WeatherAPIService()
    open_weather_service = OpenWeatherAPIService()

    def collect_weather_data(self, city):
        data = self.weather_service.get_data(city=city)
        return data['current']['temp_c']

    def collect_open_weather_data(self, city):
        data = self.open_weather_service.get_data(city=city)
        return data['main']['temp']
