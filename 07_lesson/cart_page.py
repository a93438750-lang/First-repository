from base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)
