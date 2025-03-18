import os
import allure
import pytest
from pages.auth_page import AuthPage
from utils.urls import URLs


@allure.suite("Авторизация")
class TestAuth:
    url = URLs()

    @allure.title("Авторизация пользователя")
    @pytest.mark.smoke
    def test_auth(self, driver):
        login = os.getenv("LOGIN_TEST")
        password = os.getenv("PASSWORD_TEST")
        page = AuthPage(driver)
        page.open(self.url.LOGIN_URL)
        page.login(login, password)
        with allure.step("Пользователь успешно авторизирован"):
            assert page.get_h1_project_dashboard() == "Projects Dashboard"
