import random

class Credentials:
    USER_NAME = 'Скребцова Татьяна'
    LOGIN = 'tatyanaskrebtsowa27198@yandex.com'
    PASSWORD = 'Skr280900Tatyana'

class ValidData:
    USER_NAME = 'Test test'
    LOGIN = f"Test_test{random.randint(10, 999)}@yandex.ru"
    PASSWORD = f"{random.randint(100, 999)}{random.randint(100, 999)}"