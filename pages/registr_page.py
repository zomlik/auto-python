import allure

from locators.registr_locators import RegistLocators
from pages.base_page import BasePage
from utils.data_generator import FakeData


class RegistrPage(BasePage):
    _locators = RegistLocators()
    _fake_data = FakeData()

    def registration(self,
                     username=_fake_data.username,
                     full_name=_fake_data.full_name,
                     email=_fake_data.email,
                     password=_fake_data.password
                     ):
        with allure.step('Заполнить поле Username'):
            self.find(self._locators.USERNAME_FIELD).send_keys(username)
        with allure.step('Заполнить поле Full Name"'):
            self.find(self._locators.FULL_NAME_FIELD).send_keys(full_name)
        with allure.step('Заполнить поле Email'):
            self.find(self._locators.EMAIL_FIELD).send_keys(email)
        with allure.step('Заполнить поле Password'):
            self.find(self._locators.PASSWORD_FIELD).send_keys(password)
        with allure.step('Нажать на кнопку Sing Up'):
            self.click(self._locators.SING_UP_BUTTON)

    def get_h1_project_dashboard(self):
        return self.get_text(self._locators.ASSERT_PROJECT_DASHBOARD_H1)
    
    def username_errors(self):
        return self.get_text(self._locators.USERNAME_ERRORS)
