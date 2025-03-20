from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class SlowCalculatorPage:
    """Класс для взаимодействия с медленным калькулятором на веб-странице."""

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу медленного калькулятора.

        :param driver: WebDriver, управляющий браузером.
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_time: int) -> None:
        """
        Устанавливает задержку выполнения операций в калькуляторе.

        :param delay_time: int — задержка в секундах.
        """
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(delay_time))

    def press_button(self, value: str) -> None:
        """
        Нажимает кнопку с указанным значением на калькуляторе.

        :param value: str — текст кнопки, например, '1', '+', '='.
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self, timeout: int = 50) -> str:
        """
        Ожидает появления результата на экране калькулятора.

        :param timeout: int — время ожидания результата (по умолчанию 50 секунд).
        :return: str — отображаемый результат вычислений.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text