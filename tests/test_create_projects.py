import os

import allure
import pytest

from pages.auth_page import AuthPage
from pages.create_projects_page import CreateProjectsPage
from utils.urls import URLs


@allure.suite("Создание проектов")
class TestCreateProject():
    url = URLs()

    @pytest.fixture()
    def login(self, driver):
        login = os.getenv("LOGIN_TEST")
        password = os.getenv("PASSWORD_TEST")
        page = AuthPage(driver)
        page.open(self.url.LOGIN_URL)
        page.login(login, password)
        assert page.get_h1_project_dashboard() == "Projects Dashboard"

    @allure.step("Создание проекта Scrum")
    @pytest.mark.smoke
    def test_create_scrum_project(self, driver, login):
        name = "Scrum_Project"
        page = CreateProjectsPage(driver)
        page.open(self.url.PROJECT_URL)
        page.click_new_project_button()
        page.create_scrum(name=name, description="123456789")
        with allure.step("Проект успешно создан"):
            assert page.get_h1_project_name() == "Scrum"
