import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators


class TestRegistration:

    def test_registration_new_user(self, driver, wait, random_valid_email, base_url, random_password):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN))
        driver.find_element(*AuthModalLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(random_valid_email)
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        user_name = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        assert 'User' in user_name.text

    def test_registration_invalid_email(self, driver, wait, random_invalid_email, base_url, random_password):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN))
        driver.find_element(*AuthModalLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(random_invalid_email)
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        error_message = wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_MESSAGE))
        error_field = wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_FIELD)).get_attribute('class')
        assert 'Ошибка' in error_message.text
        assert 'inputError' in error_field

    def test_registration_existing_user(self, driver, base_url, wait, existing_user):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN))
        driver.find_element(*AuthModalLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(existing_user['email'])
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(existing_user['password'])
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(existing_user['password'])
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        error_message = wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_MESSAGE))
        error_field = wait.until(EC.visibility_of_element_located(
            AuthModalLocators.ERROR_FIELD)).get_attribute('class')
        assert 'Ошибка' in error_message.text
        assert 'inputError' in error_field


        