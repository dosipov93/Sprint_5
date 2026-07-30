import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators
from constants import BASE_URL

class TestLogout:

    def test_logout_success(self, driver, wait, new_ad_data):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_FIELD)).send_keys(new_ad_data['email'])
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(new_ad_data['password'])
        driver.find_element(*AuthModalLocators.LOGIN_BTN).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        driver.find_element(*MainPageLocators.LOGOUT_BTN).click()
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BTN)).is_displayed()


