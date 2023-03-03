from pages.main_page import MainPage

'''from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.webdriver.common.by import By'''

'''def go_to_login_page(browser): # метод для открытия страницы логина
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()'''

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

