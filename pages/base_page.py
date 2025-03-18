import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открытие страницы")
    def open(self, url: str) -> str:
        return self.driver.get(url)

    @allure.step("Поиск элемента на транице")
    def find(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получение текста")
    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text

    def current_url(self):
        self.driver.current_url
