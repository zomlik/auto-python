import allure

from locators.create_projects_locators import Projects
from pages.base_page import BasePage


class CreateProjectsPage(BasePage):
    _locators = Projects()

    def click_new_project_button(self):
        with allure.step("Нажатие на кнопку New Project"):
            self.click(self._locators.NEW_PROJECT_BUTTON)

    def create_scrum(self, name, description):
        with allure.step("Нажание на проект Scrum"):
            self.click(self._locators.SCRUM_PROJECT)
        with allure.step("Заполнить поле Name"):
            self.find(self._locators.NAME_FIELD).send_keys(name)
        with allure.step("Заполнить поле Description"):
            self.find(self._locators.DESCRIPTION_FIELD).send_keys(description)
        with allure.step("Нажать на кнопку Create New Project"):
            self.click(self._locators.CREATE_PROJECT_BUTTON)
    
    def create_kanban(self, name, description):
        with allure.step("Нажатие на проект Kanban"):
            self.click(self._locators.KABAN_PROJECT)
        with allure.step("Заполнить поле Name"):
            self.find(self._locators.NAME_FIELD).send_keys(name)
        with allure.step("Заполнить поле Description"):
            self.find(self._locators.DESCRIPTION_FIELD).send_keys(description)
        with allure.step("Нажать на кнопку Create New Project"):
            self.click(self._locators.CREATE_PROJECT_BUTTON)

    def get_h1_project_name(self):
        return self.get_text(self._locators.PROJECT_NAME_H1)

    def get_h1_kanban_name(self):
        return self.get_text(self._locators.PROJECT_KANBAN_NAME)