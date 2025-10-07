'''Фикстура драйвера, запуски зарытие перед тестами, неявное ожидание'''
import pytest
from selenium import webdriver

@pytest.fixture()

def driver():
#    создали окно
    driver = webdriver.Chrome()

#    Неявные ожидания элементов

    driver.implicitly_wait(10)

#    Размер окна

    driver.maximize_window()

#    Тесты

    yield driver


    driver.quit()

