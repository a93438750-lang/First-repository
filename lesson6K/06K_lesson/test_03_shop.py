import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_shopping_flow(driver):
    """Полный автотест процесса покупки товаров на SauceDemo"""

    
    driver.get("https://www.saucedemo.com/")
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    
    assert "inventory.html" in driver.current_url, "Авторизация прошла неудачно"

    
    products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for product in products:
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'inventory_item') and .//div[text()='{product}']]/button"))
        )
        add_to_cart_button.click()

    
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert int(cart_badge.text) == len(products), f"В корзине не три товара ({cart_badge.text})"

    
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_icon.click()

    
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_products = [item.text for item in cart_items]
    assert set(cart_products) == set(products), "Некоторых товаров нет в корзине"

   
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    
    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Иванов")
    postal_code_input.send_keys("12345")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    
    total_price_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_price = total_price_element.text.split(":")[1].strip()
    assert total_price == "$58.29", f"Общая сумма неверна, получено: '{total_price}'"

    

