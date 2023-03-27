from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10): # метод, который вызывается, когда создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): # метожд открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what): # метод который перехватывает исключение. Передавать два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор)
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
