# Сохраните этот код в файл, например, test_selenium.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Устанавливаем драйвер автоматически
service = Service(ChromeDriverManager().install())

# Запускаем браузер Chrome
driver = webdriver.Chrome(service=service)

# Открываем сайт
driver.get("https://www.google.com")

# Выводим заголовок страницы в консоль
print(driver.title)

# Закрываем браузер
driver.quit()