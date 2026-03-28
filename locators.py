from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BTN = (By.XPATH, ".//button[text() = 'Вход и регистрация']") # Кнопка 'Вход и регистрация'
    USER_NAME = (By.CSS_SELECTOR, '.profileText.name') # Имя авторизированного польователя 
    LOGOUT_BTN = (By.XPATH, ".//button[text()='Выйти']") # Кнопка выхода из аккаунта

class AuthModalLocators:
    NO_ACCOUNT_BTN = (By.XPATH, ".//button[text() = 'Нет аккаунта']") # Кнопка переключения 'Нет аккаунта' в режим регистрации
    EMAIL_FIELD = (By.NAME, 'email') # Поле ввода email пользователя
    PASSWORD_FIELD = (By.NAME, 'password') # Поле ввода password пользователя
    REPEAT_PASSWORD_FIELD = (By.NAME, 'submitPassword') # Поле ввода подтверждения password пользователя
    CREATION_BUTTON = (By.XPATH, ".//button[text() = 'Создать аккаунт']") # Кнопка 'Создать аккаунт'
    HAS_ACCOUNT_BTN = (By.XPATH, ".//button[text() = 'Уже есть аккаунт']") # Кнопка переключения 'Уже есть аккаунт ' в режим авторизации
