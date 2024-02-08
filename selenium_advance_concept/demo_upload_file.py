import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://smallpdf.com/pdf-to-word")
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"C:\Apps\Python37\New Microsoft Word Document.docx")
time.sleep(20)
driver.quit()