import allure
import pytest

from pages.registr_page import RegistrPage
from utils.urls import URLs


@allure.suite("Регистрация")
class TestRegistration:
    url = URLs()

    @allure.title("Регистрация нового пользователя")
    @allure.testcase("ID-91")
    @pytest.mark.smoke
    def test_create_new_user(self, driver):
        page = RegistrPage(driver)
        page.open(self.url.REGISTRATION_URL)
        page.registration()
        with allure.step("Пользователь успешно зарегистрирован"):
            assert page.get_h1_project_dashboard() == "Projects Dashboard"

    @allure.title("Регистрация пользователя с Username состоящим из недопустимых спецсимволов")
    @allure.testcase("ID-95")
    @pytest.mark.parametrize("user", [" !@#$%^&*()"])
    def test_invalid_username_field(self, driver, user):
        page = RegistrPage(driver)
        page.open(self.url.REGISTRATION_URL)
        page.registration(username=user)
        with allure.step("Ошибка, не верно заполнено поле"):
            assert page.username_errors() == "This value seems to be invalid."
            