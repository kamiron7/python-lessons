import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации веб-драйвера перед тестом и его завершения после выполнения.
    
    :yield: WebDriver — экземпляр драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.feature("Покупка товаров")
@allure.story("Проверка процесса покупки")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления покупки на сайте")
@allure.description("Проверяет процесс покупки товара: авторизация, добавление товаров в корзину, оформление заказа.")
def test_purchase(driver):
    """
    Тест проверяет полный процесс покупки на сайте.

    - Авторизация пользователя с логином и паролем.
    - Добавление продуктов в корзину.
    - Переход в корзину и оформление заказа.
    - Проверка итоговой суммы заказа.
    """
    login_page = LoginPage(driver)

    with allure.step("Открываем страницу авторизации"):
        login_page.open()

    with allure.step("Входим в систему с логином 'standard_user' и паролем 'secret_sauce'"):
        login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    with allure.step("Добавляем товары в корзину"):
        inventory_page.add_products_to_cart()

    with allure.step("Переходим в корзину"):
        inventory_page.go_to_cart()

    cart_page = CartPage(driver)

    with allure.step("Переходим к оформлению заказа"):
        cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)

    with allure.step("Заполняем информацию для оформления заказа"):
        checkout_page.fill_checkout_info("Иван", "Петров", "12345")

    with allure.step("Получаем итоговую сумму заказа"):
        total = checkout_page.get_total_price()

    with allure.step("Проверяем итоговую сумму"):
        assert "$58.29" in total, f"Ожидалось $58.29, но получили {total}"