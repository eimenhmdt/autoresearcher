import requests
from abc import ABC, abstractmethod

class BaseWebAPIDataLoader(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def fetch_data(self, search_query, **kwargs):
        pass

    def make_request(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to fetch data from API: {response.status_code}")

