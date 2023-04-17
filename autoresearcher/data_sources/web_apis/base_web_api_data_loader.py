import requests
from abc import ABC, abstractmethod


class BaseWebAPIDataLoader(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def fetch_data(self, search_query, **kwargs):
        """
        Fetches data from the API.
        Args:
          search_query (str): The search query to use.
          **kwargs: Additional keyword arguments to pass to the API.
        Returns:
          dict: The response from the API.
        Raises:
          NotImplementedError: If the method is not implemented.
        """
        pass

    def make_request(self, endpoint, params=None):
        """
        Makes a request to the API.
        Args:
          endpoint (str): The API endpoint to make the request to.
          params (dict, optional): Additional parameters to pass to the API. Defaults to None.
        Returns:
          dict: The response from the API.
        Raises:
          Exception: If the request fails.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to fetch data from API: {response.status_code}")
