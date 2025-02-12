import allure

from methods.courier_methods import CourierMethods
from data import COURIER_NAME_FOR_LOGIN, COURIER_NAME_FOR_LOGIN_INCORRECT_PASSWORD


class TestLoginCourier:
    @allure.title('Проверяем, что можно авторизоваться')
    @allure.description('Авторизуемся с корректными данными Курьера, который есть в базе.')
    def test_login_courier_success(self):
        courier_api = CourierMethods()
        response = courier_api.login_courier(COURIER_NAME_FOR_LOGIN["login"], COURIER_NAME_FOR_LOGIN["password"])
        assert response.status_code == 200, f"Ожидался код 200, но получили {response.status_code}"
        assert response.json().get('id') == 463303

    @allure.title('Проверяем, что для авторизации нужно передать все обязательные поля')
    @allure.description('Пытаемся авторизоваться без Логина')
    def test_login_courier_without_login(self):
        courier_api = CourierMethods()
        response = courier_api.login_courier("", COURIER_NAME_FOR_LOGIN["password"])
        assert response.status_code == 400, f"Ожидался код 400, но получили {response.status_code}"
        assert response.json().get('message') == "Недостаточно данных для входа"

    @allure.title('Проверяем, что с некорректным паролем нельзя авторизоваться')
    @allure.description('Пытаемся авторизоваться с некорректным паролем')
    def test_login_courier_with_incorrect_password(self):
        courier_api = CourierMethods()
        response = courier_api.login_courier(COURIER_NAME_FOR_LOGIN_INCORRECT_PASSWORD["login"],
                                             COURIER_NAME_FOR_LOGIN_INCORRECT_PASSWORD["password"])
        assert response.status_code == 404, f"Ожидался код 404, но получили {response.status_code}"
        assert response.json().get('message') == "Учетная запись не найдена"
