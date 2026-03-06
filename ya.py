from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ya.ru/")


driver.save_screenshot('./ya.png')


driver.fullscreen_window()

sleep(15)




#driver.get("https://vk.com/")


#for x in range(1, 6):
# driver.back()
# driver.forward()

#driver.set_window_size(680, 440)

sleep(15)