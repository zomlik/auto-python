from api.api_client import ApiClient
from api.models.auth_model import Auth
from utils.urls import Routes

class TaigaApi(ApiClient):
    def __init__(self):
        super().__init__()

    def auth(self, login: str, password: str):
        self.post(endpoint=Routes.AUTH, json=Auth(
            username=login,
            password=password
        ).model_dump())
        self._headers["Authorization"] = f'Bearer {self.response_json()["auth_token"]}'
    
    @property
    def status_code(self):
        return self._response.status_code
    
    def response_json(self):
        return self._response.json()
