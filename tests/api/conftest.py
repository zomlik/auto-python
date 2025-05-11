import logging
import os

import pytest
from dotenv import load_dotenv


def pytest_addoption(parser):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    load_dotenv()


@pytest.fixture()
def get_test_user():
    return {"login": os.getenv("LOGIN_TEST"),
            "password": os.getenv("PASSWORD_TEST")}
