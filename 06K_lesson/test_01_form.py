from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    try:

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait = WebDriverWait(driver, 5)
        zip_code_field = wait.until(
                EC.presence_of_element_located((By.ID, "zip-code"))
            )
        assert (
            zip_code_field.value_of_css_property("background-color")
            == "rgba(248, 215, 218, 1)"
        ), "Zip code field is not highlighted red!"

        wait = WebDriverWait(driver, 2)

        valid_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]
        for field in valid_fields:
            element = driver.find_element(By.ID, field)
            assert (
                element.value_of_css_property("background-color")
                == "rgba(209, 231, 221, 1)"
            ), f"Field {field} is not highlighted green!"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_submission()
