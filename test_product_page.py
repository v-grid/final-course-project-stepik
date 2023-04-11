
from pages.product_page import PageObject
import time


link_product_page = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear/"


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

def test_guest_can_see_product_availability(browser):
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
def test_guest_can_go_to_product_page_see_all_element(browser):
    link = link_product_page
    page = PageObject(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_product_page()  # выполняем метод проверки того, что адрес корректный


def test_guest_can_add_product_to_basket(browser):
    link = link_product_page
    page = PageObject(browser, link)
    page.open()
    page.add_product_to_basket() # выполняем метод для добавления продукта в корзину
    page.solve_quiz_and_get_code()
    #time.sleep(30)


