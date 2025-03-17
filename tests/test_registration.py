import allure
import pytest

from pages.registr_page import RegistrPage
from utils.urls import URLs


@allure.suite("Регистрация")
class TestRegistration:
    @allure.title("Регистрация нового пользователя")
    @pytest.mark.smoke
    def test_create_new_user(self, driver):
        page = RegistrPage(driver)
        page.open(URLs.REGISTRATION_URL)
        page.registration()
        with allure.step("Пользователь успешно зарегистрирован"):
            assert page.get_h1_project_dashboard() == "Projects Dashboard"
