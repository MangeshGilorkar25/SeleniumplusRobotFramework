import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.db4free.net/")

driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()
#driver.find_element(By.XPATH, "//b[contains(text),'phpMyAdmin']").click()

driver.switch_to_window(driver.window_handles[1])

print(driver.window_handles)
time.sleep(20)
driver.quit()