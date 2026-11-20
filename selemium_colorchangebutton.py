from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
ADD_ELEMENT_BUTTON2 = ("xpath", "//button[@id='colorChange']")
button2 = driver.find_element(*ADD_ELEMENT_BUTTON2)
print(button2.value_of_css_property("color"))

initial_color = button2.value_of_css_property("color")
wait = WebDriverWait(driver, 10, poll_frequency=1)
wait.until(lambda driver: button2.value_of_css_property("color") != initial_color)

assert initial_color != button2.value_of_css_property("color")