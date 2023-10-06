import pytest
from api.wrapper_api_client import APIClientWrapper as api_methods

@pytest.mark.parametrize('currency', ('EUR', 'GBP', 'USD'))
def test_switch_currency(api_token, base_url, currency):
    response = api_methods.switch_currency(base_url=base_url, data={'currency': currency},
                                           params={'api_token': api_token})
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['success'] == "Success: Your currency has been changed!"


def test_add_cart(api_token, base_url):
    response = api_methods.add_cart(base_url=base_url, params={'api_token': api_token},
                                    data={'product_id': '40', 'quantuty': '1'},)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json['success'] == "Success: You have modified your shopping cart!"
