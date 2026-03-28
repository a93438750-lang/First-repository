
from base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.input_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
