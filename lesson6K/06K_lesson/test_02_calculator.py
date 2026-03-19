import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_functionality(driver):
    
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    
    button_7 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary'][contains(text(), '7')]"))
    )
    button_7.click()

    
    result_field = driver.find_element(By.CSS_SELECTOR, "#result")
    current_result = result_field.get_attribute("value")

    
    assert current_result == "7"

    print(f"Тест пройден успешно!")



