from urllib.parse import urlparse
'''Работа с явными ожиданиями'''
from selenium.webdriver.support.ui import WebDriverWait

'''Условия для ожиданий'''
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    '''Явное ожидание для элементов'''

    def wait_element(self, locator, timeout=10):
        """Ждет пока элемент появится в DOM """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=10):
        """Ждет пока элемент станет кликабельным """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator, timeout=10):
        """Ждет пока элемент станет видимым на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_element_present(self, locator, timeout=5):
        """Проверяет есть ли элемент на странице """
        try:
            self.wait_element(locator, timeout)
            return True
        except:
            return False