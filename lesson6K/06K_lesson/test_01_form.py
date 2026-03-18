import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

def test_simple_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("Ассистент")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    assert "error" in zip_code_field.get_attribute("class"), "Zip code должен быть красным"

    other_fields = [
        "input[name='first-name']",
        "input[name='last-name']",
        "input[name='address']",
        "input[name='email']",
        "input[name='phone']",
        "input[name='city']",
        "input[name='country']",
        "input[name='job-position']",
        "input[name='company']"
    ]

    for field_css in other_fields:
        field = driver.find_element(By.CSS_SELECTOR, field_css)
        assert "success" in field.get_attribute("class"), f"Поле {field_css} должно быть зелёным"
