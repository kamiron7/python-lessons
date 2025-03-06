import pytest
import requests
import random

BASE_URL = "https://ru.yougile.com/api-v2"
USERNAME = "kami_ron_7@mail.ru"
PASSWORD = "СКкщтфдвщ7"
COMPANY_ID = "f30b0d68-89ff-4914-91dd-10107ec35aa5"


class YougileAPI:
    """Класс для работы с API Yougile без авторизации"""

    def __init__(self, base_url, username, password, company_id):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
        self.auth_key = self._auth(username, password, company_id)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_key}",
        }

    def _auth(self, username, password, company_id):
        url = f"{self.base_url}/auth/keys"
        payload = {
            "login": username,
            "password": password,
            "companyId": company_id,
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response_json = response.json()
        key = response_json.get("key")
        return key

    def create_project(self, title):
        """Создание проекта"""
        url = f"{self.base_url}/projects"
        payload = {"title": title}
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def update_project(self, project_id, title):
        """Обновление проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        payload = {"title": title}
        response = requests.put(url, json=payload, headers=self.headers)
        return response

    def get_project(self, project_id):
        """Получение данных проекта"""
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response


@pytest.fixture(scope="module")
def api():
    """Фикстура для работы с API"""
    return YougileAPI(BASE_URL, USERNAME, PASSWORD, COMPANY_ID)


@pytest.fixture(scope="module")
def created_project(api):
    """Фикстура для создания тестового проекта"""
    project_name = f"Test Project {random.randint(1000, 9999)}"
    response = api.create_project(project_name)
    assert response.status_code == 201, "Ошибка создания проекта"
    return response.json()["id"]


def test_create_project_positive(api):
    """Позитивный тест: успешное создание проекта"""
    response = api.create_project(f"Project {random.randint(1000, 9999)}")
    assert response.status_code == 201, "Проект не был создан"
    assert "id" in response.json(), "Ответ не содержит ID проекта"


def test_update_project_positive(api, created_project):
    """Позитивный тест: успешное обновление проекта"""
    new_title = "Updated Project Name"
    response = api.update_project(created_project, new_title)
    assert response.status_code == 200, "Ошибка при обновлении проекта"


def test_get_project_positive(api, created_project):
    """Позитивный тест: успешное получение данных проекта"""
    response = api.get_project(created_project)
    assert response.status_code == 200, "Ошибка получения проекта"
    assert "id" in response.json(), "Ответ не содержит ID проекта"
    assert response.json()["id"] == created_project, "ID проекта не совпадает"


def test_create_project_negative(api):
    """Негативный тест: попытка создать проект без имени"""
    response = api.create_project("")
    assert (
        response.status_code == 400
    ), "Ожидался код 400 при создании проекта без имени"


def test_update_project_negative(api):
    """Негативный тест: обновление несуществующего проекта"""
    response = api.update_project("non-existent-id", "New Name")
    assert (
        response.status_code == 404
    ), "Ожидался код 404 при обновлении несуществующего проекта"


def test_get_project_negative(api):
    """Негативный тест: получение данных несуществующего проекта"""
    response = api.get_project("non-existent-id")
    assert (
        response.status_code == 404
    ), "Ожидался код 404 при запросе несуществующего проекта"
