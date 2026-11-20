import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
driver = webdriver.Chrome(options=options)
driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

user_agent = driver.execute_script("return navigator.userAgent")
print(user_agent)

assert "iPhone" in user_agent

assert "Android" not in user_agent
time.sleep(5)