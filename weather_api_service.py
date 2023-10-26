import requests

from api_service import APIService


class WeatherAPIService(APIService):

    def request_data(self, city):
        url = f'https://api.weatherapi.com/v1/current.json?key={self.api_token}&q={city}&aqi=no'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print('Error fetching weather data')
            print(response.content)

    def parse_data(self, data):
        return data
