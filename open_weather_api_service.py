import requests

from api_service import APIService


class OpenWeatherAPIService(APIService):

    def request_data(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_token}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
            # temp = data['main']['temp']
            # desc = data['weather'][0]['description']
            # print(f'Temperature: {temp} K')
            # print(f'Description: {desc}')
        else:
            print('Error fetching weather data')

    def parse_data(self, data):
        data['main']['temp'] -= 273.15
        return data

# {"data":
#      {"id":35538034,
#       "created_at":"2023-10-26T16:23:55Z",
#       "ticket_type":"Продажа",
#       "receipt_number":"698434463746",
#       "total_sum":1880,
#       "change":0,
#       "link":"https://app.kassa.wipon.kz/links/check/45732a19-f627-42e9-aab6-8c38c3fc7130",
#       "items":[
#           {"name":"Латте 360",
#            "price":940,
#            "quantity":1,
#            "discount":0,
#            "sum":940},
#           {"name":"Раф 360 классик",
#            "price":940,
#            "quantity":1,
#            "discount":0,
#            "sum":940}],
#       "payments":[
#           {"payment_method":1,
#            "sum":1880}],
#       "check_id":0}}