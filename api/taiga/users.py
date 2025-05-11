import allure

from api.taiga.common import TaigaApi
from utils.urls import Routes


class Users(TaigaApi):
    _endpoints = Routes()

    @allure.step("Получение статистики текущего пользователя")
    def get_me(self):
        return self.get(endpoint=self._endpoints.USERS_ME)
