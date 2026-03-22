from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
     service=ChromeService(ChromeDriverManager().install()))
 #driver.get("https://ya.ru")

# txt = driver.find_element(By.CSS_SELECTOR,'[data-statlog="2b9BAbvqv36ahq.stocks.item.300000000101470118"]').txt
# print(txt)

# teg = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2b9BAbvqv36ahq.stocks.item.300000000101470118"]').teg_name
# print(teg)

# id = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2b9BAbvqv36ahq.stocks.item.300000000101470118"]').id
# print(id)

# href = driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').get_attribute("href")
# print(href)

# ff = (driver.find_element(By.CSS_SELECTOR, '[data-statlog="2informers.stocks.item.1"]').value_of_css_property("font-family"))
# print(ff)
# driver.quit() 

# driver.get("http://uitestingplayground.com/visibility")
# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)

# driver.find_element(By.CSS_SELECTOR, "#hideButton").click()

# sleep(3)

# is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
# print(is_displayed)

# sleep(3)

# driver.quit

# driver.get("https://demoqa.com/radio-button")
# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# driver.get("https://the-internet.herokuapp.com/checkboxes")

# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
# is_selected = cb.is_selected()
# print(is_selected)

# sleep(3)

# cb.click()

# is_selected = cb.is_selected
# print(is_selected)

# driver.quit

#driver.get("https://the-internet.herokuapp.com/checkboxes")

# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# a = div.find_element(By.CSS_SELECTOR, "a")

# print(a.get_attribute("href"))

# driver.quit

# divs = driver.find_elements(By.CSS_SELECTOR, "div")
# l = len(divs)
# print(l)

# driver.get("https://the-internet.herokuapp.com/checkboxes")

# divs = driver.find_elements(By.CSS_SELECTOR, "divzxfhsf")
# print(divs)



#div = divs[6]

#css_class = div.get_attribute("class")
#print(css_class)
                            

#driver.quit

# driver.get("https://demoqa.com/browser-windows")
# driver.find_element(By.CSS_SELECTOR, "#tabButton").click()

# sleep(5)

# driver.close()

# sleep(5)

# driver.quit()
