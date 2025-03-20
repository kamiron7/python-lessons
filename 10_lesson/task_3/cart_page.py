from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для взаимодействия с корзиной покупок на веб-странице."""

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу корзины.

        :param driver: WebDriver, управляющий браузером.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self) -> None:
        """Нажимает кнопку 'Checkout' для перехода к оформлению заказа."""
        self.driver.find_element(*self.checkout_button).click()