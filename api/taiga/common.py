from api.api_client import ApiClient
from api.models.auth_model import Auth
from utils.urls import Routes


class TaigaApi(ApiClient):
    def __init__(self):
        super().__init__()

    def auth(self, login: str, password: str):
        try:
            self.post(
                endpoint=Routes.AUTH,
                json=Auth(
                    username=login,
                    password=password
            ).model_dump())

            data = self.response_json()
            
            self._headers["Authorization"] = f"Bearer {data["auth_token"]}"

        except Exception as e:
            raise RuntimeError(f"Ошибка авторизации")
