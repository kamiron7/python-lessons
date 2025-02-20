from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_time):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(delay_time))

    def press_button(self, value):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text