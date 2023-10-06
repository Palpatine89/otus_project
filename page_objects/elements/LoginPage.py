from random import randint


class Admin:
    LOGIN = 'user'
    PASSWORD = 'bitnami'


class User:
    FIRST_NAME = 'Bilbo'
    LAST_NAME = 'Testings'
    EMAIL = f'test_mail{randint(0, 1000000)}@mail.com'
    PHONE = '+79111234565'
    LOGIN = 'BOBR'
    PASSWORD = 'BOBR_123'
