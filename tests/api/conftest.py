from dotenv import load_dotenv


def pytest_addoption(parser):
    load_dotenv()