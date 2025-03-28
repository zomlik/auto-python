import pytest

from api.taiga.projects import ProjectsApi


class TestApi:
    @pytest.fixture()
    def request() -> ProjectsApi:
        return ProjectsApi()
    
    def test_api(self, request):
        request.get_list_projects()
        request.status_code