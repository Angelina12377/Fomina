from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(driver, 10, poll_frequency=1)

ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='enableAfter']")
button = wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))


assert button.is_enabled()


driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(driver, 10, poll_frequency=1)

ADD_ELEMENT_BUTTON1 = ("xpath", "//button[@id='visibleAfter']")
button1 = wait.until(EC.visibility_of_element_located(ADD_ELEMENT_BUTTON1))


assert button1.is_displayed()
