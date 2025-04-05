import allure

from api.taiga.common import TaigaApi
from utils.urls import Routes


class ProjectsApi(TaigaApi):
    _endpoints = Routes()
    
    @allure.step("Получить список проектов")
    def get_list_projects(self,
                          member=None,
                          members=None,
                          is_looking_for_people=None,
                          is_featured=None,
                          is_backlog_activated=None,
                          is_kanban_activated=None):
        return self.get(endpoint=self._endpoints.PROJECTS,
                        params={"member": member,
                                "members": members,
                                "is_looking_for_people": is_looking_for_people,
                                "is_featured": is_featured,
                                "is_backlog_activated": is_backlog_activated,
                                "is_kanban_activated": is_kanban_activated})
