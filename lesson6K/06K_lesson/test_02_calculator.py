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

    
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    
    button_7 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
    )
    button_7.click()

    
    plus_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
    )
    plus_button.click()

   
    button_8 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
    )
    button_8.click()

    
    equals_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
    )
    equals_button.click()

    
    result_field = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#result"), "15")
    )

    
    final_result = driver.find_element(By.CSS_SELECTOR, "#result").get_attribute("value")
    assert final_result == "15", f"Получен неправильный результат: {final_result}. Ожидаемый результат: 15"

    



