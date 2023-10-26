
class APIService:

    def __init__(self, api_token):
        self.api_token = api_token

    def request_data(self, city):
        raise NotImplemented()

    def parse_data(self, data):
        raise NotImplemented()

    def get_data(self, city):
        data = self.request_data(city=city)
        data = self.parse_data(data)
        return data
