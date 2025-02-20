import pytest
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    calculator = SlowCalculatorPage(driver)
    calculator.open()

    calculator.set_delay(45) 

    for btn in ["7", "+", "8", "="]:
        calculator.press_button(btn)

    assert calculator.get_result() == "15", "Ожидаемый результат 15 не появился!"