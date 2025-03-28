from abc import ABC

from requests import Session


class ApiClient(ABC):
    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip('/')
        self._session = Session()
        self._response = None
    
    def send(self, method: str, endpoint: str, **kwargs):
        url = f"{self._base_url}/{endpoint.lstrip('/')}"
        try:
            self._response = self._session.request(method, url, **kwargs)
        except Exception as e:
            raise e
    
    def get(self, endpoint: str):
        return self.send(method="GET", endpoint=endpoint)

    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass
