from api.taiga.common import TaigaApi


class ListProject:
    def __init__(self, client: TaigaApi):
        self.client = client
    
    def get_list_projects(self):
        return self.client.get(endpoint="/api/v1/projects")
    