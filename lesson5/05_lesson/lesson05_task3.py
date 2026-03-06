from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    
    driver = webdriver.Firefox()
    try:
       
        driver.get("http://the-internet.herokuapp.com/inputs")

        
        wait = WebDriverWait(driver, 10)
        input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

        
        input_field.send_keys("12345")

        
        input_field.clear()

        
        input_field.send_keys("54321")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        
        driver.quit()


run_test()
