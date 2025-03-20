import pytest
import allure
from selenium import webdriver
from form_page import FormPage


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


@allure.feature("Форма регистрации")
@allure.story("Проверка отправки формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест валидации полей формы")
@allure.description("Проверяет, что после отправки формы поля с ошибками подсвечиваются красным, а корректные — зеленым.")
def test_form_submission(driver):
    """
    Тест проверяет валидацию полей формы после отправки.

    - Поле 'zip-code' должно подсветиться красным (ошибка).
    - Остальные поля должны подсветиться зеленым (корректные данные).
    """
    page = FormPage(driver)

    with allure.step("Открываем страницу формы"):
        page.open()

    with allure.step("Заполняем и отправляем форму"):
        page.fill_form()
        page.submit()

    with allure.step("Проверяем, что поле 'zip-code' подсвечивается красным"):
        assert (
            page.get_field_color("zip-code") == "rgba(248, 215, 218, 1)"
        ), "Zip code field is not highlighted red!"

    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    with allure.step("Проверяем, что корректные поля подсвечиваются зеленым"):
        for field in fields_to_check:
            assert (
                page.get_field_color(field) == "rgba(209, 231, 221, 1)"
            ), f"Field {field} is not highlighted green!"