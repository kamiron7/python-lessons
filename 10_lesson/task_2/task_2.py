import pytest
import allure
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage


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


@allure.feature("Калькулятор")
@allure.story("Проверка работы калькулятора с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест работы медленного калькулятора")
@allure.description("Проверяет, что калькулятор правильно рассчитывает результат при задержке на каждом шаге.")
def test_slow_calculator(driver):
    """
    Тест проверяет корректность работы калькулятора при вводе последовательных действий с задержкой.

    - Задержка в 45 секунд устанавливается перед выполнением операции.
    - Проверяется, что результат операции (7 + 8) равен 15.
    """
    calculator = SlowCalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        calculator.open()

    with allure.step("Устанавливаем задержку на 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Нажимаем кнопки калькулятора: 7, +, 8, ="):
        for btn in ["7", "+", "8", "="]:
            calculator.press_button(btn)

    with allure.step("Проверяем, что результат равен 15"):
        assert calculator.get_result() == "15", "Ожидаемый результат 15 не появился!"