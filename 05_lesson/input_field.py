from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time


service = Service("./firefoxdriver/geckodriver.exe")
options = Options()
options.add_argument("--start-maximized")


driver = webdriver.Firefox(service=service, options=options)

try:

    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("1000")
    time.sleep(1)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("999")
    time.sleep(1)

finally:
    driver.quit()
