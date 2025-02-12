import requests
from urls import Urls
import allure


class CourierMethods:
    @allure.step("Авторизуемся. Логин курьера в системе")
    def login_courier(self, login, password):
        params = {"login": login, "password": password}
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}login', json=params)
        return response

    @allure.step("Создаем курьера")
    def create_courier(self, params):
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIERS_URL}', json=params)
        print(response.json())
        return response

    @allure.step("Удаляем курьера")
    def delete_courier(self, id_courier):
        response = requests.delete(f'{Urls.BASE_URL}{Urls.COURIERS_URL}{id_courier}')
        return response

    @allure.step("Получаем количество заказов курьера")
    def get_courier_orders_count(self, id_courier):
        response = requests.get(f'{Urls.BASE_URL}{Urls.BASE_URL}{id_courier}/ordersCount')
        return response

    @allure.step("Удаляем курьера, по логину и паролю (не зная id курьера)")
    def delete_courier_with_login_and_password(self, login, password):
        login_response = self.login_courier(login, password)
        login_data = login_response.json()
        courier_id = login_data.get('id')
        delete_response = self.delete_courier(courier_id)
        assert delete_response.status_code == 200, f"Не удалось удалить курьера с ID {courier_id}. Код ответа: {delete_response.status_code}"
