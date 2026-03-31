from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_REGISTER_BTN = (By.XPATH, ".//button[contains(text(), 'Вход и регистрация')]") # Кнопка 'Вход и регистрация'
    USER_NAME = (By.CSS_SELECTOR, '.profileText.name') # Имя авторизированного польователя 
    LOGOUT_BTN = (By.XPATH, ".//button[contains(text(), 'Выйти')]") # Кнопка выхода из аккаунта
    USER_AVATAR = (By.XPATH, ".//button[contains(@class, 'circleSmall')]") # Кнопка профиля
    PROFILE_ADS_BTN = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]") # Заголовок 'Мои обявления'
    LAST_AD_CARD = (By.XPATH, "(.//div[contains(@class, 'card')])[last()]") # Последнее добавленное объявление

class AuthModalLocators:
    NO_ACCOUNT_BTN = (By.XPATH, ".//button[contains(text(), 'Нет аккаунта')]") # Кнопка переключения 'Нет аккаунта' в режим регистрации
    EMAIL_FIELD = (By.NAME, 'email') # Поле ввода email пользователя
    PASSWORD_FIELD = (By.NAME, 'password') # Поле ввода password пользователя
    REPEAT_PASSWORD_FIELD = (By.NAME, 'submitPassword') # Поле ввода подтверждения password пользователя
    CREATION_BUTTON = (By.XPATH, ".//button[contains(text(), 'Создать аккаунт')]") # Кнопка 'Создать аккаунт'
    HAS_ACCOUNT_BTN = (By.XPATH, ".//button[contains(text(), 'Уже есть аккаунт')]") # Кнопка переключения 'Уже есть аккаунт ' в режим авторизации
    ERROR_MESSAGE = (By.XPATH, ".//span[contains(text(), 'Ошибка')]") # Текст с ошибкой 'Ошибка'
    ERROR_FIELD = (By.CSS_SELECTOR, "[class*='input_inputError']") # Идентификация класса с ошибкой 'Поля ввода выделены красным'
    LOGIN_BTN = (By.XPATH, ".//button[contains(text(), 'Войти')]") # Кнопка авторизации 

class CreateAdLocators:
    CREATE_AD_BTN = (By.XPATH, ".//button[contains(text(), 'Разместить объявление')]") # Кнопка 'Разместить объявление' 
    CREATE_AD_MODAL = (By.XPATH, ".//h1[contains(text(), 'авторизуйтесь')]") # Модальное окно 'Авторизируйтесь что бы разместить объявление'
    ITEM_NAME_FIELD = (By.NAME, 'name') # Поле ввода названия обэвления
    CONDITION_NEW_RADIO = (By.XPATH, ".//div[contains(@class, 'radioUnput_input')]/label[contains(text(), Новый)]") # Состояние RabioButton - 'Новый'
    CONDITION_USED_RADIO = (By.XPATH, "//label[text()='Б/У']") # Состояние RabioButton - 'Б/У'
    PRICE_FIELD = (By.NAME, 'price') # Поле ввода 'Стоимость'
    SUBMIT_BTN = (By.XPATH, ".//button[contains(text(), 'Опубликовать')]") # Кнопка Опубликовать
    CITIES_DROPDOWN_BTN = (By.XPATH, './/button[contains(@class, "dropDownMenu")]') # Кнопка выпадающего списка выобора города 'dropdown'
    SELECT_CITY_BTN = (By.XPATH, ".//span[contains(text(), 'Нижний Новгород')]/parent::button") # Кнопка выбора конкретного города 'Нижний новгород'
    CATEGORY_DROPDOWN_BTN = (By.XPATH, ".//input[contains(@name , 'category')]/following-sibling::button") # Выпадающий список , выбора категории объявления 
    SELECT_CATEGORY_BTN = (By.XPATH, ".//span[contains(text(), 'Технологии')]/parent::button") # Кнопка выбора конкретной категории 'Технологии'
    DESCRIPTION_FIELD = (By.XPATH, ".//textarea[contains(@name,'description')]") # Поле ввода 'Описание'
    ARROW_BTN = (By.XPATH, ".//svg[@class='arrow']/parent::button") # Кнопка перехода к следующим обявлениям 