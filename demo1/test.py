import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(30)

driver.get('https://www.facebook.com')

# time.sleep(5)
driver.find_element(By.ID, "email").send_keys("mangeshgilorkar@gmail.com")
driver.find_element(By.ID, "pass").send_keys("1232224242")
# driver.find_element(By.NAME, "login").click()
# time.sleep(5)
driver.find_element(By.LINK_TEXT, "Create new account").click()
# time.sleep(5)
driver.find_element(By.NAME, "firstname").send_keys("efkhfdf")
# time.sleep(5)
driver.find_element(By.NAME, "lastname").send_keys("QQQQQQQQQQQ")

driver.find_element(By.ID, "password_step_input").send_keys("1212121212")
# time.sleep(5)
driver.find_element(By.XPATH, "//input[@value='-1']").click()
driver.find_element(By.XPATH, "//label[text()='Custom']").click()

selectDay = Select(driver.find_element(By.ID, "day"))
selectDay.select_by_visible_text("20")

selectMonth = Select(driver.find_element(By.ID, "month"))
selectMonth.select_by_visible_text("Dec")

selectYear = Select(driver.find_element(By.ID, "year"))
selectYear.select_by_visible_text("2000")
time.sleep(5)

# time.sleep(5)
print(driver.title)

print(driver.current_url)

# time.sleep(5)
driver.quit()
