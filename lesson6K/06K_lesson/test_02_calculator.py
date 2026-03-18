from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  


btn_7 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "span.btn.btn-outline-primary"))
)
btn_7.click()


btn_7 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary'][contains(text(), '7')]"))
)
btn_7.click()


btn_7 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='btn btn-outline-primary']//font[contains(text(), '7')]"))
)
btn_7.click()


btn_7 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn-outline-primary') and contains(., '7')]"))
)
btn_7.click()


btn_7 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "span.btn-outline-primary"))
)
btn_7.click()


driver.quit()

