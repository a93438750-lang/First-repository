from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        wait = WebDriverWait(driver, 10)
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Button with Dynamic ID']"))
        )
        button.click()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

for i in range(3):
    run_test()
    time.sleep(3)




