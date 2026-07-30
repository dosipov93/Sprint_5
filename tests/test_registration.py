import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators
from constants import BASE_URL

class TestRegistration:

    def test_registration_new_user(self, driver, wait, random_valid_email, random_password):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN)).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(random_valid_email)
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME)).is_displayed()

    def test_registration_invalid_email(self, driver, wait, random_invalid_email, random_password):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN)).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(random_invalid_email)
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_MESSAGE)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_FIELD)).is_displayed()

    def test_registration_existing_user(self, driver, wait, new_ad_data):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN)).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(new_ad_data['email'])
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(new_ad_data['password'])
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(new_ad_data['password'])
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_MESSAGE)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_FIELD)).is_displayed()
        

        