from datetime import datetime

import allure
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
    options.add_argument("--disable-notifications")
    return options


@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        browser = item.funcargs["driver"]
        allure.attach(browser.get_screenshot_as_png(),
                      name=f"Screenshot {datetime.now()}",
                      attachment_type=allure.attachment_type.PNG)
