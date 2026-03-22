from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    blue_button.click()

    updated_button_text = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.ID, "updatingButton").text
    )

    expected_text = "SkyPro"
    if updated_button_text == expected_text:
        print(expected_text)
    

finally:
    driver.quit()




