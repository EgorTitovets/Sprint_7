import allure

from methods.courier_methods import CourierMethods
from data import COURIER_NAME_BASE, COURIER_NAME_FOR_DUPLICATE_COURIER, COURIER_NAME_WITHOUT_LOGIN


class TestCreateCourier:

    @allure.title('Проверяем, что курьера можно создать')
    @allure.description('Создаем нового курьера, с новыми/корректными данными.')
    def test_create_courier_success(self):
        courier_api = CourierMethods()
        response = courier_api.create_courier(COURIER_NAME_BASE)
        assert response.status_code == 201, f"Ожидался код 201, но получили {response.status_code}"
        assert response.json().get('ok') == True, f"Ответ API: {response.json()}"
        courier_api.delete_courier_with_login_and_password(COURIER_NAME_BASE["login"], COURIER_NAME_BASE["password"])

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьера')
    @allure.description('Создаем курьера с данным, которые уже есть в базе.')
    def test_create_create_same_courier_twice(self):
        courier_api = CourierMethods()
        response = courier_api.create_courier(COURIER_NAME_FOR_DUPLICATE_COURIER)
        assert response.status_code == 409, f"Ожидался код 409, но получили {response.status_code}"
        assert response.json().get('message') == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверяем, что нельзя создать курьера без одного из обязательных полей')
    @allure.description('Пытаемся создать курьера Без логина')
    def test_create_without_login(self):
        courier_api = CourierMethods()
        response = courier_api.create_courier(COURIER_NAME_WITHOUT_LOGIN)
        assert response.status_code == 400, f"Ожидался код 400, но получили {response.status_code}"
        assert response.json().get('message') == "Недостаточно данных для создания учетной записи"
