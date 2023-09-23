import requests


class RequestManager:
    '''
    Класс для отправки запросов на API
    '''

    BASE_URL = 'https://fakestoreapi.com'

    def get(self, endpoint: str):
        response = requests.get(self.BASE_URL + endpoint)
        return response.json()

