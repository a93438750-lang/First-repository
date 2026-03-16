from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

try:
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
    )

    
    images = driver.find_elements(By.CSS_SELECTOR, "img")

    
    if len(images) >= 3:
        
        third_image_src = images[2].get_attribute("src")
        
        print(third_image_src)
    


finally:
    driver.quit()