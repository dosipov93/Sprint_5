import pytest
import uuid
import random
import string
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver 
    driver.quit()


@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 7)

@pytest.fixture()
def base_url():
    return 'https://qa-desk.stand.praktikum-services.ru/'

@pytest.fixture()
def profile_url():
    return 'https://qa-desk.stand.praktikum-services.ru/profile'

@pytest.fixture()
def random_valid_email():
    return uuid.uuid4().hex[:7]+'@yandex.ru'

@pytest.fixture()
def random_invalid_email():
    return uuid.uuid4().hex[:7]+'yandex.u'

@pytest.fixture()
def random_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(9))

@pytest.fixture()
def existing_user():
    return {
        'email': 'test_user999@yandex.ru',
        'password': 'Test123',
    }

@pytest.fixture
def random_price():
    return random.randint(1000, 999999)

@pytest.fixture()
def create_add_list(random_price):
    return {
        'item_name': 'Монитор',
        'description': 'Продаётся игровой монитор, торг уместен!',
        'price': str(random_price)
    }

