from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://uitestingplayground.com/ajax")
try:
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "bg-success"))
        )

    print(alert.text)
finally:
    driver.quit()
