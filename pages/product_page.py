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
        assert "?promo=" in self.browser.current_url, "URL product_link is not presented" # проверка, что в url адресе есть слово ?promo=newYear


    def should_be_product_name(self):

        assert self.is_element_present(*ProductPage.PRODUCT_NAME), "Product name is not presented"# проверка, что есть название товара


    def collect_product_name(self):
        global product_name
        product_name = self.browser.find_element(*ProductPage.PRODUCT_NAME).text


    def should_be_product_price(self):
        assert self.is_element_present(*ProductPage.PRODUCT_PRICE), "Product price is not presented"  # проверка, что есть стоимость товара


    def collect_product_price(self):
        global product_price
        product_price = self.browser.find_element(*ProductPage.PRODUCT_PRICE).text


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


    def should_see_message_about_added_product_to_basket(self):
        assert "был добавлен" in (self.browser.find_element(*ProductPage.PRODUCT_ADDED_TO_BASKET)).text, "The product is not added in basket"  # проверка, что есть сообщение о добавлении продукта в корзину


    def name_of_product_in_basket_correct(self):
        #print(product_name)
        #print(self.browser.find_element(*ProductPage.PRODUCT_ADDED_TO_BASKET).text)
        assert product_name == self.browser.find_element(*ProductPage.PRODUCT_ADDED_TO_BASKET).text, "The name of the product in the basket does not match the name on the product page" #in self.browser.find_element(*ProductPage.PRODUCT_ADDED_TO_BASKET).text, "The name of the product in the basket does not match the name on the product page" # проверка, что имя продукта в корзине соответсвует имени на странице продукта

    def price_of_product_in_basket_correct(self):
        #print(product_price)
        #print(self.browser.find_element(*ProductPage.PRICE_OF_BASKET).text)
        assert product_price in self.browser.find_element(*ProductPage.PRICE_OF_BASKET).text, "The price of the product in the basket does not match the price on the product page"  # проверка, что стоимость продукта в корзине соответсвует стоимости на странице продукта
