import requests
from api.endpoints import Endpoints


class APIClientWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def switch_currency(base_url, endpoint=Endpoints.CURRENCY, params=None, data=None, headers=None):
        """"""
        url = base_url + endpoint
        response = requests.post(url=url, params=params, data=data, headers=headers)
        return response

    @staticmethod
    def cart_action(base_url, endpoint, params=None, data=None, headers=None):
        """"""
        url = base_url + endpoint
        response = requests.post(url=url, params=params, data=data, headers=headers)
        return response
