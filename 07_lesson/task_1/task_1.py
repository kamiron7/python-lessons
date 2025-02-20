import pytest
from selenium import webdriver
from form_page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_form_submission(driver):
    page = FormPage(driver)
    page.open()
    page.fill_form()
    page.submit()

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
    for field in fields_to_check:
        assert (
            page.get_field_color(field) == "rgba(209, 231, 221, 1)"
        ), f"Field {field} is not highlighted green!"
