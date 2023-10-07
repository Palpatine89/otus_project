class Endpoints:
    """Класс с доступными конечными точками"""
    LOGIN = '/index.php?route=api/login'
    CURRENCY = '/index.php?route=api/currency'
    CART_ADD = '/index.php?route=api/cart/add'
    CART_REMOVE = '/index.php?route=api/cart/remove'
    CART_PRODUCTS = '/index.php?route=api/cart/products'
    APPLY_COUPON = '/index.php?route=api/coupon'
    APPLY_VOUCHER = '/index.php?route=api/voucher'
    ADD_VOUCHER = '/index.php?route=api/voucher/add'
    SET_CUSTOMER = '/index.php?route=api/customer'
    SET_SHIPPING_ADDRESS = '/index.php?route=api/shipping/address'
    RETURN_AVALIABLE_SHIPPING_METHODS = '/index.php?route=api/shipping/methods'
    SET_SHIPPING_METHOD = '/index.php?route=api/shipping/method'
    RETURN_AVALIABLE_PAYMENTS_METHODS = '/index.php?route=api/payment/methods'
    SET_PAYMENT_ADDRESS = '/index.php?route=api/payment/address'
    SET_AVALIABLE_PAYMENT_METHOD = '/index.php?route=api/payment/method'
