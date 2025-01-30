from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

try:
    wait = WebDriverWait(driver, 10)
    wait.until(
        lambda d:
        len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4
    )
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(f"Third image src = {third_image_src}")
    else:
        print("Недостаточно изображений на странице")
finally:
    driver.quit()
