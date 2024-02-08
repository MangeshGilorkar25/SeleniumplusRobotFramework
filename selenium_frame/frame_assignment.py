"""
Task 2
1.  Navigate onto http://demo.openemr.io/b/openemr/
2.  Update username as admin
3.  Update password as pass
4.  Select language as English (Indian)
5.  Click on the login button
6.  Click on Patient  Click New Search
7.  Add the first name, last name
8.  Update DOB as today's date
driver.findElement(By.id("form_DOB")).sendKeys("2024-01-12");
9.  Update the gender
10. . Click on the create new patient button above the form
11. . Click on confirm create new patient button.
12. . Print the text from alert box (if any error before handling alert add 5 sec wait)
13. . Handle alert
14. Close the Happy Birthday popup
15. Get the added patient name and print in the console.

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://demo.openemr.io/b/openemr/")

time.sleep(20)
driver.quit()
