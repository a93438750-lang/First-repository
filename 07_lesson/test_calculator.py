import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import time

class TestCalculator:

    @pytest.fixture(autouse=True)
    def setup(self):
        
        self.driver = webdriver.Chrome()
        self.calculator_page = CalculatorPage(self.driver)
        yield
        
        self.driver.quit()

    def test_calculator_functionality(self):
        
        self.calculator_page.open()

        
        self.calculator_page.set_delay("45")

        
        self.calculator_page.click_button_7()
        self.calculator_page.click_plus()
        self.calculator_page.click_button_8()
        self.calculator_page.click_equals()

        
        time.sleep(46)

        
        result = self.calculator_page.get_result()
        assert result == "15", f"Ожидаемый результат: 15, фактический: {result}"
