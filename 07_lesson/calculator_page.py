from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_FIELD = (By.CSS_SELECTOR, ".screen")

    def open(self):
        
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        
        delay_input = self.wait.until(EC.element_to_be_clickable(self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button_7(self):
        
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_7))
        button.click()

    def click_plus(self):
        
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLUS))
        button.click()

    def click_button_8(self):
        
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_8))
        button.click()

    def click_equals(self):
        
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_EQUALS))
        button.click()

    def get_result(self):
        
        result = self.wait.until(EC.presence_of_element_located(self.RESULT_FIELD))
        return result.text
