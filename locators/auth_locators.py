from selenium.webdriver.common.by import By


class AuthLotators:
    LOGIN_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    ASSERT_PROJECT_DASHBOARD_H1 = (By.CSS_SELECTOR, ".duty-summary h1")
