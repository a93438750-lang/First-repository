import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_simple_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    
    data = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phoneNumber": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "jobPosition": "Ассистент",
        "company": "SkyPro"
    }

    
    for field_name, value in data.items():
        input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[name='{field_name}']")))
        input_field.clear()
        input_field.send_keys(value)

   
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    
    zip_code_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='zipCode']")))
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Поле Zip Code не выделено красным"

    
    valid_fields = list(data.keys())  
    for field_name in valid_fields:
        field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[name='{field_name}']")))
        assert "is-invalid" not in field.get_attribute("class"), f"Поле {field_name} ошибочно отмечено как ошибочное"

    
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))
    assert "Please fill out this field." in error_message.text, "Сообщение об ошибке не появилось"

    
    assert submit_button.is_enabled(), "Кнопка отправки стала неактивной"


@pytest.mark.parametrize("field_name,test_value,expected_class", [
    ("firstName", "Иван", "is-valid"),
    ("lastName", "Петров", "is-valid"),
    ("address", "Ленина, 55-3", "is-valid"),
    ("city", "Москва", "is-valid"),
    ("country", "Россия", "is-valid"),
    ("jobPosition", "Ассистент", "is-valid"),
    ("company", "SkyPro", "is-valid"),
])
def test_field_validation(driver, field_name, test_value, expected_class):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    
    field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[name='{field_name}']")))
    field.clear()
    field.send_keys(test_value)

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    
    assert expected_class in field.get_attribute("class"), f"Поле {field_name} не получило класс {expected_class}"


def test_required_fields(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    
    error_messages = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='alert']")))
    assert len(error_messages) >= 1 