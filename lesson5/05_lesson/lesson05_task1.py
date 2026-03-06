from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/classattr")
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        button_xpath = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert text: '{alert_text}'")
        alert.accept()
        print("Test passed successfully!\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
        print("Browser closed.\n")

if __name__ == "__main__":
    print("Test run 1 of 3")
    run_test()
    time.sleep(3)

    print("Test run 2 of 3")
    run_test()
    time.sleep(3)

    print("Test run 3 of 3")
    run_test()

    print("All three runs completed!")

