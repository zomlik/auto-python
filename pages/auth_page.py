import allure

from locators.auth_locators import AuthLotators
from pages.base_page import BasePage


class AuthPage(BasePage):
    _locators = AuthLotators()

    def login(self, login, password):
        with allure.step("Заполнить поле Login"):
            self.find(self._locators.LOGIN_FIELD).send_keys(login)
        with allure.step("Заполнить поле Password"):
            self.find(self._locators.PASSWORD_FIELD).send_keys(password)
        with allure.step("Нажать на кнопку Login"):
            self.click(self._locators.LOGIN_BUTTON)

    def get_h1_project_dashboard(self):
        return self.get_text(self._locators.ASSERT_PROJECT_DASHBOARD_H1)
