import os


class URLs:
    MAIN_PAGE = os.getenv("BASE_URL")
    LOGIN_URL = f"{MAIN_PAGE}/login"
    REGISTRATION_URL = f"{MAIN_PAGE}/register"
    PROJECT_URL = f"{MAIN_PAGE}/projects"


class Routes:
    AUTH = "/auth"
    REGISTRY = "/auth/register"
    PROJECTS = "/projects"
    USERS = "/users"
    USERS_ME = "/users/me"
