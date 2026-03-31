import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators


class TestLogout:

    def test_logout_success(self, driver, wait, base_url, existing_user):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_FIELD))
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(existing_user['email'])
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(existing_user['password'])
        driver.find_element(*AuthModalLocators.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        driver.find_element(*MainPageLocators.LOGOUT_BTN).click()
        login_register_btn = wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BTN))
        assert 'Вход и регистрация' in login_register_btn.text


