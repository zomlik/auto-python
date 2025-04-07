import allure

from api.taiga.common import TaigaApi
from utils.urls import Routes


class ProjectsApi(TaigaApi):
    _endpoints = Routes()
    
    @allure.step("Получить список проектов")
    def get_list_projects(self,
                          member=None,  # member id
                          members=None,  # member ids
                          is_looking_for_people=None,  # the project is looking for new members
                          is_featured=None,  # the project has been highlighted by the instance staff
                          is_backlog_activated=None,  # backlog is active
                          is_kanban_activated=None  # kanban is active
                          ): 
        return self.get(endpoint=self._endpoints.PROJECTS,
                        params={"member": member,
                                "members": members,
                                "is_looking_for_people": is_looking_for_people,
                                "is_featured": is_featured,
                                "is_backlog_activated": is_backlog_activated,
                                "is_kanban_activated": is_kanban_activated})
