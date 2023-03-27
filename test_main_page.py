from pages.main_page import MainPage
from pages.login_page import LoginPage


'''from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.webdriver.common.by import By'''



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

def test_guest_can_see_login_url(browser):
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.should_be_login_url()

def test_guest_can_see_login_form(browser):
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.should_be_login_form()

def test_guest_can_see_register_form(browser):
    link = link_page
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.should_be_register_form()


