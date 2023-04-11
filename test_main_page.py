import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage



link_page = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    link = link_page
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # после перехода получаем текущий адркс, чтобы дальше его использовать для методов в классе LoginPage
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page() # при запуске этого метода будут выполнены все 3 теста из файла login_page.py
                                # также, методы можно вызывать по отдельности, чтобы разделить их на разные тесты

@pytest.mark.skip
def test_guest_can_see_login_url(browser): # входит в проверку should_be_login_page, можно закомментировать
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    login_page.should_be_login_url()

@pytest.mark.skip
def test_guest_can_see_login_form(browser): # входит в проверку should_be_login_page, можно закомментировать
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.should_be_login_form()

def test_guest_can_see_register_form(browser): # входит в проверку should_be_login_page, можно закомментировать
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.should_be_register_form()

