import allure

from methods.order_methods import OrderMethods


class TestListOrders:

    @allure.title('Получение списка заказов')
    @allure.description("Проверяем, что API возвращает список заказов и он содержит необходимые поля")
    def test_get_orders_list(self):
        order_api = OrderMethods()
        response = order_api.get_order_lists_all()
        json_response = response.json()
        assert response.status_code == 200, f"Ожидался код 200, но получили {response.status_code}"
        assert "orders" in json_response, f"В ответе нет ключа 'orders': {json_response}"
        assert "id" in json_response["orders"][0] and "courierId" in json_response["orders"][
            0], f"В заказе нет ключа 'id' и 'courierId': {json_response['orders'][0]}"
