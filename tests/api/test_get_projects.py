import allure
import pytest

from http import HTTPStatus
from api.taiga.projects import ProjectsApi


@allure.suite("Проекты API")
class TestGetProjectsApi:
    @allure.title("Получить список всех публичных проектов без фильтров")
    @allure.testcase("ID-101")
    @pytest.mark.smoke
    def test_get_all_projects(self):
        r = ProjectsApi()
        r.get_list_projects()
        assert r.status_code == HTTPStatus.OK
        