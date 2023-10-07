import pytest
from api.wrapper_api_client import APIClientWrapper as api_methods
from api.endpoints import Endpoints

PRODUCT_ID_IPHONE = 40
COUPON_ID_FREE_SHIPPING = 3333


@pytest.fixture(scope="function")
def add_product_to_cart(api_token, base_url):
    # Добавление товара в корзину
    api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_ADD,
                            params={'api_token': api_token},
                            data={'product_id': PRODUCT_ID_IPHONE, 'quantuty': '1'})

    # Получение идентификатора корзины с добавленным товаром
    response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_PRODUCTS,
                                       params={'api_token': api_token})
    cart_id = response.json()['products'][0]['cart_id']

    yield response.json()

    # Удаление добавленного товара
    api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_REMOVE,
                                params={'api_token': api_token}, data={'key': cart_id})


def remove_product_from_cart(api_token, base_url):
    # Получение идентификатора корзины с добавленным товаром
    response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_PRODUCTS,
                                       params={'api_token': api_token})
    cart_id = response.json()['products'][0]['cart_id']

    # Удаление добавленного товара
    api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_REMOVE,
                            params={'api_token': api_token}, data={'key': cart_id})


class TestOpenCartApiTests:
    @pytest.mark.parametrize('currency', ('EUR', 'GBP', 'USD', 'RU'))
    def test_switch_currency(self, api_token, base_url, currency):
        response = api_methods.switch_currency(base_url=base_url, data={'currency': currency},
                                               params={'api_token': api_token})
        resp_json = response.json()
        assert response.status_code == 200
        if currency == 'RU':
            assert resp_json['error'] == 'Warning: Currency code is invalid!'
        else:
            assert resp_json['success'] == "Success: Your currency has been changed!"

    def test_add_cart(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_ADD,
                                           params={'api_token': api_token},
                                           data={'product_id': PRODUCT_ID_IPHONE, 'quantuty': '1'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == "Success: You have modified your shopping cart!"

        # Удаление созданных данных
        remove_product_from_cart(api_token, base_url)

    def test_add_cart_no_data_product_id(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_ADD,
                                           params={'api_token': api_token},
                                           data={'product_id': 9999, 'quantuty': '1'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['error']['store'] == 'Product can not be bought from the store you have choosen!'

    def test_products_cart(self, api_token, base_url, add_product_to_cart):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_PRODUCTS,
                                           params={'api_token': api_token})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json == add_product_to_cart

    def test_remove_cart(self, api_token, base_url, add_product_to_cart):
        cart_id = add_product_to_cart['products'][0]['cart_id']
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.CART_REMOVE,
                                           params={'api_token': api_token}, data={'key': cart_id})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == "Success: You have modified your shopping cart!"

    def test_apply_coupon(self, api_token, base_url, add_product_to_cart):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.APPLY_COUPON,
                                           params={'api_token': api_token}, data={'coupon': COUPON_ID_FREE_SHIPPING})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == 'Success: Your coupon discount has been applied!'

    def test_apply_invalid_coupon(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.APPLY_COUPON,
                                           params={'api_token': api_token}, data={'coupon': COUPON_ID_FREE_SHIPPING})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['error'] == "Warning: Coupon is either invalid, expired or reached it's usage limit!"

    def test_apply_invalid_voucher(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.APPLY_VOUCHER,
                                           params={'api_token': api_token}, data={'voucher': 'VOU-7179'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['error'] == 'Warning: Gift Voucher is either invalid or the balance has been used up!'

    def test_add_voucher(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.ADD_VOUCHER,
                                           params={'api_token': api_token},
                                           data={'from_name': 'MyOpenCart Admin',
                                                 'from_email': 'admin@example.com',
                                                 'to_name': 'Dear Customer',
                                                 'to_email': 'customer@example.com',
                                                 'amount': '100',
                                                 'code': 'VOU-7177'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == 'Success: You have modified your shopping cart!'

    def test_apply_voucher(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.APPLY_VOUCHER,
                                           params={'api_token': api_token}, data={'voucher': 'VOU-7177'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == 'Success: Your gift voucher discount has been applied!'

    def test_set_customer(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_CUSTOMER,
                                           params={'api_token': api_token},
                                           data={'firstname': 'Dear',
                                                 'lastname': 'Customer',
                                                 'email': 'customer@example.com',
                                                 'telephone': '+1 879 2548022'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == 'You have successfully modified customers'

    def test_set_shipping_address(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_SHIPPING_ADDRESS,
                                           params={'api_token': api_token},
                                           data={'firstname': 'Customer',
                                                 'lastname': 'Dear',
                                                 'address_1': 'Somewhere',
                                                 'city': 'KLD',
                                                 'country_id': 'RUS',
                                                 'zone_id': 'KGD'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json == []

    def test_return_avaliable_shipping_methods(self, api_token, base_url, add_product_to_cart):
        api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_SHIPPING_ADDRESS,
                                params={'api_token': api_token},
                                data={'firstname': 'Customer',
                                      'lastname': 'Dear',
                                      'address_1': 'Somewhere',
                                      'city': 'KLD',
                                      'country_id': '1',
                                      'zone_id': 'KAB'})
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.RETURN_AVALIABLE_SHIPPING_METHODS,
                                           params={'api_token': api_token})
        resp_json = response.json()['shipping_methods']['flat']
        assert response.status_code == 200
        assert resp_json['title'] == 'Flat Rate'
        assert resp_json['sort_order'] == '1'

    def test_set_shipping_method(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_SHIPPING_METHOD,
                                           params={'api_token': api_token},
                                           data={'shipping_method': 'pickup.pickup'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json == []

    def test_return_avaliable_payment_methods(self, api_token, base_url, add_product_to_cart):
        api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_PAYMENT_ADDRESS,
                                params={'api_token': api_token},
                                data={'firstname': 'Customer',
                                      'lastname': 'Dear',
                                      'address_1': 'Somewhere',
                                      'city': 'KLD',
                                      'country_id': '1',
                                      'zone_id': 'KAB'})
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.RETURN_AVALIABLE_PAYMENTS_METHODS,
                                           params={'api_token': api_token})
        resp_json = response.json()['payment_methods']['cod']
        assert response.status_code == 200
        assert resp_json['code'] == 'cod'
        assert resp_json['title'] == 'Cash On Delivery'
        assert resp_json['terms'] == ''
        assert resp_json['sort_order'] == '5'

    def test_set_payment_address(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_PAYMENT_ADDRESS,
                                           params={'api_token': api_token},
                                           data={'firstname': 'Customer',
                                                 'lastname': 'Dear',
                                                 'address_1': 'Somewhere',
                                                 'city': 'KLD',
                                                 'country_id': 'RUS',
                                                 'zone_id': 'KGD'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['success'] == 'Success: Payment address has been set!'

    def test_set_payment_method(self, api_token, base_url):
        response = api_methods.cart_action(base_url=base_url, endpoint=Endpoints.SET_AVALIABLE_PAYMENT_METHOD,
                                           params={'api_token': api_token},
                                           data={'payment_method': 'bank_transfer'})
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json == []