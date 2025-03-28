from api.taiga.common import TaigaApi
from utils.urls import Routes


class ProjectsApi(TaigaApi):
    _endpoints = Routes()
    
    def get_list_projects(self):
        return self.get(endpoint=self._endpoints.PROJECTS)
