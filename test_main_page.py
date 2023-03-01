import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import time


def go_to_login_page(browser): # метод для открытия страницы логина
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)

class MainPage():