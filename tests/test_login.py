import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators

class TestLogin:

    def test_login_success(self, driver, base_url, wait, existing_user):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_FIELD))
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(existing_user['email'])
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(existing_user['password'])
        driver.find_element(*AuthModalLocators.LOGIN_BTN).click()
        user_name = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        assert 'User' in user_name.text
        driver.delete_all_cookies()


        