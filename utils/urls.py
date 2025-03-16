import os


class URLs:
    MAIN_PAGE = os.getenv("BASE_URL")
    REGISTRATION_URL = f"{MAIN_PAGE}/register"
