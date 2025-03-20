from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для взаимодействия со страницей оформления заказа."""

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу оформления заказа.

        :param driver: WebDriver, управляющий браузером.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        :param first: str — имя покупателя.
        :param last: str — фамилия покупателя.
        :param zip_code: str — почтовый индекс.
        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: str — итоговая сумма заказа в формате текста.
        """
        return self.driver.find_element(*self.total_price).text