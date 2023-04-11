from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import NoAlertPresentException
import math

class PageObject(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_product_availability()
        self.should_be_button_review()
        self.should_be_button_to_basket()



    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url, "URL product_link is not presented" # проверка, что в url адресе есть слово ?promo=newYear


    def should_be_product_name(self):
        assert self.is_element_present(*ProductPage.PRODUCT_NAME), "Product name is not presented"# проверка, что есть название товара

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPage.PRICE_PRICE), "Product price is not presented"  # проверка, что есть стоимость товара

    def should_be_product_availability(self):
        availability = self.browser.find_element(*ProductPage.PRODUCT_AVAILABILITY)
        assert "На складе" in availability.text, "The product is not in stock"  # проверка, что товар есть на складе
        assert "доступно" in availability.text, "The product is not available"  # проверка, что товар доступен в некотором количестве

    def should_be_button_review(self):
        assert self.is_element_present(*ProductPage.WRITE_REVIEW), "There is no button for writing a product review"  # проверка, что есть кнопка для написания отзыва

    def should_be_button_to_basket(self):
        assert self.is_element_present(*ProductPage.PRODUCT_ADD_BUTTON_TO_BASKET), "There is no button to add a product to the basket"  # проверка, что есть кнопка для добавления в корзину

    def add_product_to_basket(self):
        button_to_basket = self.browser.find_element(*ProductPage.PRODUCT_ADD_BUTTON_TO_BASKET)
        button_to_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")