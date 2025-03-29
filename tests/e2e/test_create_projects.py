import os

import allure
import pytest

from pages.auth_page import AuthPage
from pages.create_projects_page import CreateProjectsPage
from utils.urls import URLs


@allure.suite("Создание проектов")
class TestCreateProject:
    url = URLs()

    @pytest.fixture()
    def login(self, driver):
        login = os.getenv("LOGIN_TEST")
        password = os.getenv("PASSWORD_TEST")
        page = AuthPage(driver)
        page.open(self.url.LOGIN_URL)
        page.login(login, password)
        assert page.get_h1_project_dashboard() == "Projects Dashboard"

    @allure.title("Создание проекта Scrum")
    @allure.testcase("ID-97")
    @pytest.mark.smoke
    def test_create_scrum_project(self, driver, login):
        page = CreateProjectsPage(driver)
        page.open(self.url.PROJECT_URL)
        page.click_new_project_button()
        page.create_scrum(name="Scrum Project", description="123456789")
        with allure.step("Проект успешно создан"):
            assert page.get_h1_project_name() == "Scrum"
    
    @allure.title("Создание проекта Kanban")
    @allure.testcase("ID-98")
    @pytest.mark.smoke
    def test_create_kanban_project(self, driver, login):
        page = CreateProjectsPage(driver)
        page.open(self.url.PROJECT_URL)
        page.click_new_project_button()
        page.create_kanban(name="Kanban Project", description="123456789")
        with allure.step("Проект успешно создан"):
            assert page.get_h1_kanban_name() == "Kanban"
