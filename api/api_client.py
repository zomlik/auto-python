import os
from abc import ABC
from http import HTTPMethod

from requests import Session
from requests.exceptions import RequestException

from utils.logger import log


class ApiClient(ABC):
    def __init__(self):
        self._base_url = os.getenv("BASE_API")
        self._session = Session()
        self._response = None
        self._headers = {}
    
    def _send(self, method: str, endpoint: str, **kwargs):
        url = f"{self._base_url}/{endpoint.lstrip('/')}"
        try:
            self._response = self._session.request(method, url, **kwargs, verify=False)
            log(self._response, json=self._response.json())
            return self._response
        except RequestException as e:
            raise e
    
    def get(self, endpoint: str, params: dict = None):
        return self._send(method=HTTPMethod.GET,
                          endpoint=endpoint,
                          params=params,
                          headers=self._headers)

    def post(self, endpoint: str, json: dict = None):
        return self._send(method=HTTPMethod.POST,
                          endpoint=endpoint,
                          json=json,
                          headers=self._headers)

    def put(self, endpoint: str, json: dict = None):
        return self._send(method=HTTPMethod.PUT,
                          endpoint=endpoint,
                          json=json,
                          headers=self._headers)
    
    def delete(self, endpoint: str):
        return self._send(method=HTTPMethod.DELETE, endpoint=endpoint)
