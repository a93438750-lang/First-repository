from base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, first_name):
        self.input_text(self.FIRST_NAME_FIELD, first_name)

    def fill_last_name(self, last_name):
        self.input_text(self.LAST_NAME_FIELD, last_name)

    def fill_postal_code(self, postal_code):
        self.input_text(self.POSTAL_CODE_FIELD, postal_code)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def get_total_price(self):
        total_element = self.find_element(self.TOTAL_PRICE)
        return total_element.text
