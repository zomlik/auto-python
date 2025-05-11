import allure
from pydantic import BaseModel, ValidationError
from api.api_client import ApiClient
from api.models.auth_model import Auth
from utils.urls import Routes


class TaigaApi(ApiClient):
    def __init__(self):
        super().__init__()

    @allure.step("Выполнение авторизации")
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

        except Exception:
            raise RuntimeError("Ошибка авторизации")
    
    @allure.step("Получение id текущего пользователя")
    def get_current_user_id(self):
        self.get(endpoint=Routes.USERS_ME)
        data = self.response_json()["id"]
        return data

    def check_json_shema(self, model: BaseModel, json_data):
        try:
            model(**json_data)
        except ValidationError:
            raise
