import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators


class TestRegistration:

    def test_registration_new_user(self, driver, wait, random_valid_email, base_url, random_password):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_BTN).click()
        driver.find_element(*AuthModalLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(random_valid_email)
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        assert 'User' in driver.find_element(*MainPageLocators.USER_NAME).text