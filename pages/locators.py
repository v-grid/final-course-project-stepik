from selenium.webdriver.common.by import By

class MainPageUrl():
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # селектор для поиска ссылки на страницу авторизации

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # селектор для поиска формы авторизации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # селектор для поиска формы регистрации

class ProductPage():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main  h1") # селектор для поиска названия продукта на странице
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".alert:nth-last-child(3)  strong") # селектор для поиска названия продукта в корзине
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color") # селектор для поиска стоимости продукта на странице
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong") # селектор для поиска стоимости продукта в корзине
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, ".instock.availability")  # селектор для поиска наличия продукта
    WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review") # селектор для поиска кнопки формы отзыва о продукте
    PRODUCT_ADD_BUTTON_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")  # селектор для поиска кнопки добавления продукта в корзину
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert:nth-last-child(3)  strong")  # селектор для поиска сообщения о добавлении продукта в корзину
    PRICE_OF_BASKET = (By.CSS_SELECTOR, ".alertinner p strong") # селектор для поиска сообщения о стоимости корзины




