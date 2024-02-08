import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
# driver.implicitly_wait(30)
time.sleep(5)
driver.get('https://www.medibuddy.in/')

# time.sleep(5)

time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "×").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Login").click()
# driver.find_element(By.ID, "UserLastName").send_keys("wick")
# driver.find_element(By.ID, "UserEmail-WGTb").send_keys("john@gmail.com")
time.sleep(5)
# time.sleep(5)
driver.quit()
