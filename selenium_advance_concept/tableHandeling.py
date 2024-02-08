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
driver.get("https://datatables.net/extensions/select/examples/initialisation/checkbox.html")
action = webdriver.ActionChains(driver)

# Click on the checkbox when name is matching with "Brenden Wagner"
for i in range(1, 11):
    name1 = driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[2]").text
    if name1 == "Brenden Wagner":
        driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[1]").click()


time.sleep(10)
driver.quit()
