from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

try: 
    driver.get('http://uitestingplayground.com/ajax')
    
    
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ajaxButton'))
    )
    button.click()
    
    
    result_div = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success'))
    )
    
    
    actual_text = result_div.text
    
    
    expected_text = "Data loaded with AJAX get request."
    if actual_text == expected_text:
        print(expected_text)

finally:   
    driver.quit()
