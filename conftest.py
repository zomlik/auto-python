import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--ci", action="store_true", help="Запустить браузер в headless режиме")
    load_dotenv()


@pytest.fixture()
def chrome_options(request):
    options = Options()
    if request.config.getoption("ci"):
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    return options


@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()
