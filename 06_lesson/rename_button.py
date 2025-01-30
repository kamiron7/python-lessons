from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://uitestingplayground.com/textinput")
try:
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    wait = WebDriverWait(driver, 10)
    updated_button = wait.until(
        lambda d: d.find_element(By.ID, "updatingButton").text == "SkyPro"
    )

    button = driver.find_element(By.ID, "updatingButton")
    print(f"New button name: {button.text}")
finally:
    driver.quit()
