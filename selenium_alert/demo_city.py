import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.online.citibank.co.in/")

driver.find_element(By.XPATH, "//a[@class='newclose']").click()
driver.find_element(By.XPATH, "//a[@class='newclose2']").click()
driver.find_element(By.XPATH, "//span[@class='txtSign']").click()
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "//div[@class='fl cup pt3']").click()
driver.find_element(By.XPATH, "//a[text()='select your product type']").click()
# driver.find_element(By.LINK_TEXT, "select your product type").click()
driver.find_element(By.XPATH, "//a[text()='Credit Card']").click()
# driver.find_element(By.LINK_TEXT, "Credit Card").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'select your product type').click()
driver.find_element(By.ID, "citiCard1").send_keys("4545")
driver.find_element(By.ID, "citiCard2").send_keys("5656")
driver.find_element(By.ID, "citiCard3").send_keys("8887")
driver.find_element(By.ID, "citiCard4").send_keys("9998")

driver.find_element(By.NAME, "CCVNO").send_keys("122")

driver.find_element(By.NAME, "DOB").click()

# selectYear = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
# selectYear.select_by_value("2022")
# selectMonth = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
# selectMonth.select_by_visible_text("Apr")
#
# selectDay = Select(driver.find_element(By.LINK_TEXT, "ui-state-default ui-state-active ui-state-hover"))
# selectDay.select_by_visible_text("4")
# # driver.find_element(By.XPATH, "//img[@alt='Go']").click()
# Enter date of birth as “14/04/2022”

driver.find_element(By.XPATH, "//input[@name='DOB']").click()
# select year as 2022
select_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
select_year.select_by_visible_text("2022")
# select month as Apr
select_month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
select_month.select_by_visible_text("Apr")
# select date 14
driver.find_element(By.XPATH, "(//a[@class='ui-state-default'])[14]").click()

time.sleep(20)

# driver.quit()
# actual_alert_text = driver.switch_to.alert.text
# print(actual_alert_text)
# driver.switch_to.alert.accept()
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.alert_is_present())
#
# time.sleep(20)
# driver.quit()
# # click on go
