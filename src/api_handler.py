import requests
from urllib.parse import urlencode, urljoin


class ApiHandler:
    """ 
    Handles API connection
    """
    def __init__(self, url: str, params: dict, api_token: str) -> None:
        self.base_url = url
        self.params = params
        self.token = api_token


    def encode_url(self) -> str:
        """
        Encodes URL parameters and concatenates them to the base URL.
        """
        encoded_params = urlencode(self.params)
        final_url = urljoin(self.base_url, '?' + encoded_params)
        return final_url

    
    def fetch_data(self) -> dict:
        """
        Fetches the project summary from the API using a POST request.
        """
        payload = {}
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.request("POST", self.encode_url(), headers=headers, data=payload)
        
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                pass
        else:
            raise Exception(f"Failed to retrieve data from API. Status code: {response.status_code}")
        
        response_dict = response.json()
        return response_dict
 