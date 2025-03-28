from api.api_client import ApiClient


class TaigaApi(ApiClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def auth(self, login: str, password: str):
        pass
    