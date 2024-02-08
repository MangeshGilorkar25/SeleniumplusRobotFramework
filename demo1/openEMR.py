from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.openemr.io/b/openemr/interface/login/login.php?site=default")
time.sleep(1)
driver.implicitly_wait(15)
driver.find_element(By.ID,"authUser").send_keys("admin")
driver.find_element(By.ID,"clearPass").send_keys("pass")
lang = Select(driver.find_element(By.XPATH,'//select[@name="languageChoice"]'))
lang.select_by_value("18")
time.sleep(1)
driver.find_element(By.ID,"login-button").click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[contains(text(),"Patient")]').click()
driver.find_element(By.XPATH,'//div[contains(text(),"New/Search")]').click()
time.sleep(1)
#driver.find_element(By.XPATH,'//span[contains(text(),"Search or Add Patient")]').click()
driver.switch_to.frame("pat")
driver.find_element(By.ID,"form_fname").send_keys("Jason")
driver.find_element(By.ID,"form_lname").send_keys("Thompsson")
driver.find_element(By.ID,"form_DOB").send_keys("2/1/2024")
gender = Select(driver.find_element(By.XPATH,'//select[@name="form_sex"]'))
gender.select_by_value("Male")
time.sleep(1)
driver.find_element(By.XPATH,'//button[@id="create"]').click()

# Click on confirm create new patient button
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH,"//button[@value='true']").click()


time.sleep(1)
driver.switch_to.default_content()
wait=WebDriverWait(driver,15)
wait.until(expected_conditions.alert_is_present())
time.sleep(5)
Alert(driver).accept()
driver.switch_to.default_content()
time.sleep(1)
driver.find_element(By.XPATH,'//div[@class="closeDlgIframe"]').click()
time.sleep(1)
name = driver.find_element(By.XPATH,'//span[@data-bind="text: pname()"]')
print("Patient Name ==> "+name.text)
time.sleep(3)
driver.quit()