from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс для взаимодействия со страницей каталога товаров."""

    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу каталога.

        :param driver: WebDriver, управляющий браузером.
        """
        self.driver = driver
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self) -> None:
        """Добавляет несколько товаров в корзину."""
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.bolt_tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину, нажимая на значок корзины."""
        self.driver.find_element(*self.cart_icon).click()