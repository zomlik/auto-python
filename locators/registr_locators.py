from selenium.webdriver.common.by import By


class RegistLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    FULL_NAME_FIELD = (By.XPATH, "//input[@name='full_name']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SING_UP_BUTTON = (By.CSS_SELECTOR, "button")
    ASSERT_PROJECT_DASHBOARD_H1 = (By.CSS_SELECTOR, ".duty-summary h1")
