import uuid
import random
import string


def generate_valid_email():
    return uuid.uuid4().hex[:6]+'@yandex.ru'

def generate_invalid_email():
    return uuid.uuid4().hex[:7] + 'yandex.u'

def generate_password():
    chars = string.ascii_letters + string.digits + '!@#$%'
    return ''.join(random.choice(chars) for _ in range (8))

def generate_data():
    return {
        'email': 'test_user999@yandex.ru',
        'password': 'Test123',
        'item_name': 'Монитор',
        'description': 'Продаётся  монитор 144Гц, торг уместен!',
        'price': str(random.randint(1000, 99999))
    }


