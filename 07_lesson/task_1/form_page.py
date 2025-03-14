from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url =\
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_form(self):
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

    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()

    def get_field_color(self, field_name):
        element = self.driver.find_element(By.ID, field_name)
        return element.value_of_css_property("background-color")