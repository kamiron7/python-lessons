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

    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    time.sleep(1)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()
    time.sleep(2)

finally:

    driver.quit()
