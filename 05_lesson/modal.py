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

    driver.get("http://the-internet.herokuapp.com/entry_ad")
    time.sleep(2)

    close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
    close_button.click()

    time.sleep(2)

finally:

    driver.quit()
