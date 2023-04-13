import pytest
from pages.product_page import PageObject
import time



link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear/"


def test_guest_can_go_to_product_page(browser):
    link = link_product_page
    page = PageObject(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_product_url()  # выполняем метод проверки того, что адрес корректный


def test_guest_can_see_product_name(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.should_be_product_name()


def test_guest_can_see_product_price(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.should_be_product_price()

@pytest.mark.skip
def test_guest_can_see_product_availability(browser): # only for the Russian-language site
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.should_be_product_availability()


def test_guest_can_see_button_review(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.should_be_button_review()


def test_guest_can_see_button_to_basket(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.should_be_button_to_basket()



@pytest.mark.skip
def test_guest_can_go_to_product_page_see_all_element(browser): # only for the Russian-language site
    link = link_product_page
    page = PageObject(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_product_page()  # выполняем метод проверки того, что адрес корректный


@pytest.mark.parametrize('link', ["0","1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser, link)
    page.open()
    page.collect_product_name()
    page.collect_product_price()
    page.add_product_to_basket()  # выполняем метод для добавления продукта в корзину
    page.solve_quiz_and_get_code()
    page.name_of_product_in_basket_correct()  # выполняем метод для сравнения названия продукта в корзине и на странице товара
    page.price_of_product_in_basket_correct()  # выполняем метод для сравнения стоимости продукта в корзине и на странице товара



@pytest.mark.skip
def test_guest_can_see_message_about_added_product_to_basket(browser): # only for the Russian-language site
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.add_product_to_basket()  # выполняем метод для добавления продукта в корзину
    page.solve_quiz_and_get_code()
    page.should_see_message_about_added_product_to_basket() # выполняем метод для проверки наличия сообщения о добалении продукта


def test_name_of_product_in_basket_correct(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.collect_product_name()
    page.add_product_to_basket()  # выполняем метод для добавления продукта в корзину
    page.solve_quiz_and_get_code()
    page.name_of_product_in_basket_correct()  # выполняем метод для сравнения названия продукта в корзине и на странице товара



def test_cost_of_product_in_basket_correct(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.collect_product_price()
    page.add_product_to_basket()  # выполняем метод для добавления продукта в корзину
    page.solve_quiz_and_get_code()
    page.price_of_product_in_basket_correct()  # выполняем метод для сравнения стоимости продукта в корзине и на странице товара
    #time.sleep(5)


