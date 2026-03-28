from base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    BACKPACK_ADD_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Backpack']/following::button")
    BOLT_TSHIRT_ADD_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/following::button")
    ONESIE_ADD_BUTTON = (By.XPATH, "//div[text()='Sauce Labs Onesie']/following::button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.click_element(self.BACKPACK_ADD_BUTTON)

    def add_bolt_tshirt_to_cart(self):
        self.click_element(self.BOLT_TSHIRT_ADD_BUTTON)

    def add_onesie_to_cart(self):
        self.click_element(self.ONESIE_ADD_BUTTON)

    def go_to_cart(self):
        self.click_element(self.CART_ICON)
