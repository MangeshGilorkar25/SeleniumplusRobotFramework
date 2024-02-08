# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
# print(driver.title)
# driver.find_element(By.XPATH, "//input[@name='UserFirstName']").send_keys("John")
# driver.find_element(By.XPATH, "//input[@name='UserLastName']").send_keys("Wick")
# driver.find_element(By.XPATH, "//input[@name='UserEmail']").send_keys("john@gmail.com")
# selectJobTitle = Select(driver.find_element(By.NAME, "UserTitle"))
# selectJobTitle.select_by_visible_text("IT Manager")
# selectEmployee = Select(driver.find_element(By.NAME, "CompanyEmployees"))
# selectEmployee.select_by_visible_text("101 - 200 employees")
# selectCountry = Select(driver.find_element(By.NAME, "CompanyCountry"))
# selectCountry.select_by_visible_text("United Kingdom")
# driver.find_element(By.XPATH, "//div[@class='field valid']//div[@class='checkbox-ui']").click()
# driver.find_element(By.XPATH, "//button[@name='start my free trial']").click()
# time.sleep(5)
# # driver.find_element(By.NAME,"UserEmail").send_keys("john@gmail.com")


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
print(driver.title)
driver.find_element(By.XPATH, "//input[@name='UserFirstName']").send_keys("John")
driver.find_element(By.XPATH, "//input[@name='UserLastName']").send_keys("Wick")
driver.find_element(By.XPATH, "//input[@name='UserEmail']").send_keys("john@gmail.com")
selectJobTitle = Select(driver.find_element(By.NAME, "UserTitle"))
selectJobTitle.select_by_visible_text("IT Manager")
selectEmployee = Select(driver.find_element(By.NAME, "CompanyEmployees"))
selectEmployee.select_by_visible_text("101 - 200 employees")


selectCountry = Select(driver.find_element(By.NAME, "CompanyCountry"))
selectCountry.select_by_visible_text("United Kingdom")
driver.find_element(By.XPATH, "//div[@class='field valid']//div[@class='checkbox-ui']").click()

driver.find_element(By.XPATH, "//button[@name='start my free trial']").click()
time.sleep(5)
# driver.find_element(By.NAME,"UserEmail").send_keys("john@gmail.com")
