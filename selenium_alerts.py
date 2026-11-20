import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

##Первый алерт на странице
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/alerts")
alertbutton1=driver.find_element(by=By.XPATH,value="//*[@id='alertButton']")
alertbutton1.click()

alert =driver.switch_to.alert
print(alert.text)
assert alert.text == "You clicked a button"
alert.accept()

##Алерт появляется через 5 сек
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/alerts")
alertbutton2=driver.find_element(by=By.XPATH,value="//*[@id='timerAlertButton']")
alertbutton2.click()
wait = WebDriverWait(driver, 10, poll_frequency=1)
wait.until(EC.alert_is_present())

alert2 = driver.switch_to.alert
print(alert2.text)
assert alert2.text == "This alert appeared after 5 seconds"
alert2.accept()