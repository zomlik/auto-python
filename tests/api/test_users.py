from http import HTTPStatus

import allure

from api.taiga.users import Users
from api.models.users_models import ResponseUser


@allure.suite("Пользователи API")
class TestUsers:
    @allure.title("Получить статистику аккаунта пользователя")
    @allure.testcase("ID-170")
    def test_get_stats_current_user(self, get_test_user):
        r = Users()
        r.auth(login=get_test_user["login"], password=get_test_user["password"])
        r.get_me()
        r.check_json_shema(model=ResponseUser, json_data=r.response_json())
        assert r.status_code == HTTPStatus.OK
        assert r.response_json()["username"] == get_test_user["login"]
