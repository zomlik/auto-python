from api.api_client import ApiClient


class TaigaApi(ApiClient):
    def __init__(self):
        super().__init__()

    def auth(self, login: str, password: str):
        pass

    @property
    def status_code(self):
        return self._response.status_code
    
    def response_json(self):
        return self._response.json()
    
