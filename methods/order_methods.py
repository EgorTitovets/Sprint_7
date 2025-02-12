import allure
import requests
from urls import Urls


class OrderMethods:

    @allure.step("Создаем заказ")
    def create_order(self, order_data):
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_URL}', json=order_data)
        return response

    @allure.step("Принимаем заказ")
    def accept_order(self, order_number, id_courier):
        response = requests.put(f'{Urls.BASE_URL}{Urls.ORDERS_URL}accept/{order_number}?courierId={id_courier}')
        return response

    @allure.step('Получаем заказ по его номеру')
    def get_order_by_number(self, order_number):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_URL}track?t={order_number}')
        return response

    @allure.step('Получаем список заказов курьера')
    def get_orders_list(self, id_courier):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_URL}?courierId={id_courier}')
        return response

    @allure.step('Отменяемм заказ')
    def cancel_order(self, order_number):
        response = requests.put(f'{Urls.BASE_URL}{Urls.BASE_URL}cancel?track={order_number}')
        return response

    @allure.step('Завершаем заказ')
    def finish_order(self, order_number):
        response = requests.put(f'{Urls.BASE_URL}{Urls.ORDERS_URL}finish/{order_number}')
        return response

    @allure.step('Получаем список Всех заказов')
    def get_order_lists_all(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_URL}')
        return response
