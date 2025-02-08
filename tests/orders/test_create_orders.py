import allure
import pytest

from methods.order_methods import OrderMethods
from data import ORDER_DATA_SCOOTER_BLACK, ORDER_DATA_SCOOTER_GREY, ORDER_DATA_SCOOTER_BLACK_AND_GREY, \
    ORDER_DATA_SCOOTER_WITHOUT_SCOOTER_COLOR


@pytest.mark.parametrize(
    "order_data, order_name",
    [
        (ORDER_DATA_SCOOTER_BLACK, "Чёрный самокат"),
        (ORDER_DATA_SCOOTER_GREY, "Серый самокат"),
        (ORDER_DATA_SCOOTER_BLACK_AND_GREY, "Чёрный и серый самокат"),
        (ORDER_DATA_SCOOTER_WITHOUT_SCOOTER_COLOR, "Заказ без указания цвета"),
    ]
)
def test_create_order_success(order_data, order_name):
    allure.dynamic.title(f"Создание заказа - {order_name}")
    order_api = OrderMethods()
    response = order_api.create_order(order_data)
    assert response.status_code == 201, f"Ожидался код 201, но получили {response.status_code}"
    assert "track" in response.json(), f"В ответе нет ключа 'track': {response.json()}"
