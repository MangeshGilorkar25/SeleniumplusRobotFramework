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

# elements = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
# row_count = len(elements)
#
# # Click on the checkbox when name is matching with "Brenden Wagner"
# for j in range(1, 6):
#     driver.find_element(By.LINK_TEXT, "paginate_button next").click()
#     for i in range(1, row_count):
#         name1 = driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{i}]/td[2]").text
#         print(name1)


totalrows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
print(totalrows)
totalnumofrows = len(totalrows)
print(totalnumofrows)
for i in range(1, 6):
    driver.find_element(By.XPATH,f"//a[text()='{i}']").click()
    for j in range(1, totalnumofrows):
        name1 = driver.find_element(By.XPATH, f"//table[@id='example']/tbody/tr[{j}]/td[2]").text
        print(name1)


time.sleep(10)
driver.quit()
