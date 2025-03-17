import allure

from locators.registr_locators import RegistLocators
from pages.base_page import BasePage
from utils.data_generator import FakeData


class RegistrPage(BasePage):
    _locators = RegistLocators()
    _fake_data = FakeData()

    def registration(self,
                     username=None,
                     full_name=None,
                     email=None,
                     password=None
                     ):
        with allure.step('Заполнить поле "username"'):
            self.find(self._locators.USERNAME_FIELD).send_keys(
                self._fake_data.username if username is None else username
            )
        with allure.step('Заполнить поле "full_name"'):
            self.find(self._locators.FULL_NAME_FIELD).send_keys(
                self._fake_data.full_name if full_name is None else full_name
            )
        with allure.step('Заполнить поле "email"'):
            self.find(self._locators.EMAIL_FIELD).send_keys(
                self._fake_data.email if email is None else email
            )
        with allure.step('Заполнить поле "password"'):
            self.find(self._locators.PASSWORD_FIELD).send_keys(
                self._fake_data.password if password is None else password
            )
        with allure.step('Нажать на кнопку "Sing Up"'):
            self.click(self._locators.SING_UP_BUTTON)

    def get_h1_project_dashboard(self):
        return self.get_text(self._locators.ASSERT_PROJECT_DASHBOARD_H1)
