from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    """Класс для взаимодействия с формой на веб-странице."""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы формы.

        :param driver: WebDriver, управляющий браузером.
        """
        self.driver = driver
        self.url = \
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self) -> None:
        """Открывает страницу формы в браузере."""
        self.driver.get(self.url)

    def fill_form(self) -> None:
        """Заполняет форму тестовыми данными."""
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }
        for field, value in data.items():
            self.driver.find_element(By.NAME, field).send_keys(value)

    def submit(self) -> None:
        """Отправляет форму, нажимая на кнопку 'Submit'."""
        self.driver.find_element(By.CSS_SELECTOR,
        "button[type='submit']").click()

    def get_field_color(self, field_name: str) -> str:
        """
        Получает цвет фона указанного поля формы.

        :param field_name: str — имя поля (ID элемента).
        :return: str — цвет фона элемента в формате CSS
            (например, 'rgba(255, 0, 0, 1)').
        """
        element = self.driver.find_element(By.ID, field_name)
        return element.value_of_css_property("background-color")
