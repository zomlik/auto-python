from selenium.webdriver.common.by import By


class Projects:
    NEW_PROJECT_BUTTON = (By.XPATH, "//a[contains(text(), 'New project')]")

    SCRUM_PROJECT = (By.XPATH, "//p[contains(text(), 'Scrum')]")
    KABAN_PROJECT = (By.XPATH, "//p[contains(text(), 'Kanban')]")
    DUBLICATE_PROJECT = (By.XPATH, "//p[contains(text(), 'Duplicate project')]")

    NAME_FIELD = (By.XPATH, "//input[@name='project-name']")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea")
    CREATE_PROJECT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create Project')]")

    PROJECT_NAME_H1 = (By.CSS_SELECTOR, ".backlog header h1")
    PROJECT_KANBAN_NAME = (By.CSS_SELECTOR, "header h1 span")
