from selenium.webdriver.common.by import By

class MainPageUrl():
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # селектор для поиска ссылки на страницу авторизации

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # селектор для поиска формы авторизации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # селектор для поиска формы регистрации
