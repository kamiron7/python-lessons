from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()

service = Service("./chromedriver-win64/chromedriver.exe")


driver = webdriver.Chrome(service=service, options=options)

try:

    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    time.sleep(2)

    add_button = driver.find_element(
        By.XPATH,
        "//button[text()=\
    'Add Element']",
    )
    for _ in range(5):
        add_button.click()
        time.sleep(0.5)

    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    print(f"Количество кнопок 'Delete' на странице: {len(delete_buttons)}")

finally:

    driver.quit()
