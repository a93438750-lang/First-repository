from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")

element = driver.find_element(By.CSS_SELECTOR, "#text")
element.send_keys("test skypro")
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


sleep(10)

driver.quit()
