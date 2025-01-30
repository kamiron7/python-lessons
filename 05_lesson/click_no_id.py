from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


service = Service("./chromedriver-win64/chromedriver.exe")
options = Options()
options.add_argument("--start-maximized")


driver = webdriver.Chrome(service=service, options=options)

try:

    driver.get("http://uitestingplayground.com/dynamicid")

    button = driver.find_element(
        By.XPATH,
        "//button\
    [contains(@class, 'btn-primary')]",
    )
    button.click()

    time.sleep(2)

finally:

    driver.quit()
