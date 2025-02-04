import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    try:

        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        for button in ["7", "+", "8", "="]:
            driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        result_text = driver.find_element(By.CLASS_NAME, "screen").text
        assert (
            result_text == "15"
        ), f"Ожидаемый результат: 15, но получено: {result_text}"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main()
