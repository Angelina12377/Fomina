import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)

firstName = driver.find_element("xpath", "//input[@id='userName']")
time.sleep(5)
firstName.clear()
firstName.send_keys("Angelina")
time.sleep(5)

userEmail = driver.find_element("xpath", "//input[@id='userEmail']")
time.sleep(5)
userEmail.clear()
userEmail.send_keys("angelina.r76@mail.ru")
time.sleep(5)

currentAddress = driver.find_element("xpath", "//textarea[@id='currentAddress']")
time.sleep(5)
currentAddress.send_keys(Keys.COMMAND + "A")
currentAddress.send_keys(Keys.BACKSPACE)
currentAddress.send_keys("South Africa, Ballito")
time.sleep(5)

assert firstName.get_attribute("value") == "Angelina"
assert userEmail.get_attribute("value") == "angelina.r76@mail.ru"
assert currentAddress.get_attribute("value") == "South Africa, Ballito"
print(firstName.get_attribute("value"))
print(userEmail.get_attribute("value"))
print(currentAddress.get_attribute("value"))