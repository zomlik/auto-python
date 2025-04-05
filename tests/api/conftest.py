import logging

from dotenv import load_dotenv


def pytest_addoption(parser):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    load_dotenv()
    