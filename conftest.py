import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from helpers import generate_data, generate_invalid_email, generate_password, generate_valid_email

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.delete_all_cookies()
    driver.quit()
    
@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 7)

@pytest.fixture()
def random_valid_email():
    return generate_valid_email()

@pytest.fixture()
def random_invalid_email():
    return generate_invalid_email()

@pytest.fixture()
def random_password():
    return generate_password()

@pytest.fixture()
def new_ad_data():
    return generate_data()
