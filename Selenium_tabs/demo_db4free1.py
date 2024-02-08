import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.db4free.net/")

driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()
# driver.find_element(By.XPATH, "//b[contains(text),'phpMyAdmin']").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID, "input_username").send_keys("admin")
driver.find_element(By.ID, "input_password").send_keys("admin1233")
driver.find_element(By.ID, "input_go").click()
time.sleep(5)
actual_error = driver.find_element(By.ID, "pma_errors").text
time.sleep(5)
print(driver.window_handles)
print(actual_error)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.quit()
