import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://google.com/")

#driver.find_element(By.XPATH, "//div[text()='Accept all']").click()

elements = driver.find_elements(By.XPATH, "//a")
print(len(elements))
total_ele = len(elements)

for i in range(0, total_ele):
    actual_text = elements[i].text
    print(actual_text)
    href = elements[i].get_attribute("href")
    print(href)

time.sleep(10)
driver.quit()
