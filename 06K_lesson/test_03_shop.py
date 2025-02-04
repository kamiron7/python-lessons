import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_swag_shop():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        items = \
            [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]
        for item in items:
            driver.find_element(
                By.XPATH,
                f"//div[text()='{item}']\
                /ancestor::div[@class='inventory_item']//button",
            ).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total_price = (
            WebDriverWait(driver, 10)
            .until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "summary_total_label")
                )
            )
            .text
        )

        assert (
            "$58.29" in total_price
        ), f"Ожидаемая сумма: $58.29, но получено: {total_price}"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main()
