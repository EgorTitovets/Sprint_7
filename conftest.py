import pytest
from data import COURIER_NAME_BASE
from methods.courier_methods import CourierMethods

@pytest.fixture()
def courier():
    response = CourierMethods().create_courier(COURIER_NAME_BASE)
    login_response = CourierMethods().login_courier(COURIER_NAME_BASE["login"], COURIER_NAME_BASE["password"])
    login_data = login_response.json()
    courier_id = login_data.get('id')
    if courier_id:
        yield courier_id
    else:
        pytest.fail(f"Ответ при логине не содержит 'id': {login_data}")
    delete_response = CourierMethods().delete_courier(courier_id)