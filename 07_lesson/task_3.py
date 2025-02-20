from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self):
        self.driver.find_element(*self.backpack).click()
        self.driver.find_element(*self.bolt_tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first, last, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_purchase(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Иван", "Петров", "12345")
    total = checkout_page.get_total_price()

    assert "$58.29" in total, f"Ожидалось $58.29, но получили {total}"
