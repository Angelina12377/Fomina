import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")
uploadFile=driver.find_element(by=By.XPATH,value="//*[@id='uploadFile']")
uploadFile.send_keys(r"/Users/etienne/PycharmProjects/Fomina/selenium_fileload")
time.sleep(1)

print(uploadFile.get_attribute("value"))
assert "selenium_fileload" in uploadFile.get_attribute("value")
print(f"success")