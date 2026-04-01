import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthModalLocators, CreateAdLocators


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver, wait, base_url,):
        driver.get(base_url)
        driver.find_element(*CreateAdLocators.CREATE_AD_BTN).click()
        create_ad_modal = wait.until(EC.visibility_of_element_located(CreateAdLocators.CREATE_AD_MODAL))
        assert 'Чтобы разместить' in create_ad_modal.text

    def test_create_ad_authorized(self, driver, wait, base_url, profile_url, random_valid_email, random_password, create_add_list):
        driver.get(base_url)
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.NO_ACCOUNT_BTN))
        driver.find_element(*AuthModalLocators.NO_ACCOUNT_BTN).click()
        wait.until(EC.visibility_of_element_located(AuthModalLocators.EMAIL_FIELD))
        driver.find_element(*AuthModalLocators.EMAIL_FIELD).send_keys(random_valid_email)
        driver.find_element(*AuthModalLocators.PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.REPEAT_PASSWORD_FIELD).send_keys(random_password)
        driver.find_element(*AuthModalLocators.CREATION_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        driver.find_element(*CreateAdLocators.CREATE_AD_BTN).click()
        driver.find_element(*CreateAdLocators.ITEM_NAME_FIELD).send_keys(create_add_list['item_name'])
        radio_input = driver.find_element(*CreateAdLocators.CONDITION_USED_RADIO)
        driver.execute_script("arguments[0].scrollIntoView();", radio_input)
        driver.execute_script("arguments[0].click();", radio_input)
        driver.find_element(*CreateAdLocators.CITIES_DROPDOWN_BTN).click()
        select_city_btn = driver.find_element(*CreateAdLocators.SELECT_CITY_BTN)
        driver.execute_script('arguments[0].scrollIntoView();', select_city_btn)
        driver.execute_script('arguments[0].click();', select_city_btn)
        driver.find_element(*CreateAdLocators.CATEGORY_DROPDOWN_BTN).click()
        select_category_btn = driver.find_element(*CreateAdLocators.SELECT_CATEGORY_BTN)
        driver.execute_script('arguments[0].scrollIntoView();', select_category_btn)
        driver.execute_script('arguments[0].click();', select_category_btn)
        driver.find_element(*CreateAdLocators.DESCRIPTION_FIELD).send_keys(create_add_list['description'])
        driver.find_element(*CreateAdLocators.PRICE_FIELD).click()
        driver.find_element(*CreateAdLocators.PRICE_FIELD).send_keys(create_add_list['price'])
        driver.find_element(*CreateAdLocators.SUBMIT_BTN).click()
        driver.get(profile_url)
        profile_ads_btn = wait.until(EC.presence_of_element_located(MainPageLocators.PROFILE_ADS_BTN))
        driver.execute_script('arguments[0].scrollIntoView();', profile_ads_btn)
        last_ad_card = wait.until(EC.visibility_of_element_located(MainPageLocators.LAST_AD_CARD))
        assert create_add_list['price'] in last_ad_card.text.replace(' ', '')
        

