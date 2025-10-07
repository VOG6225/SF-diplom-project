
from .base_page import BasePage
from .locators import Locators
from config import *


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, auth_url)

        driver.get(auth_url)
        '''Заголовок Авторизация'''
        self.authorization = self.wait_element(Locators.header_card_title, 10)
        '''Лого РТ'''
        self.logo = self.wait_visible(Locators.logo, 10)
        '''Заголовок у лого'''
        self.rt_info_title = self.wait_visible(Locators.rt_info_title, 10)
        '''Инф. текст у лого'''
        self.rt_info_text = self.wait_visible(Locators.rt_info_text, 10)
        '''Элемент меню телефон'''
        self.btn_phone = self.wait_clickable(Locators.btn_phone, 10)
        '''Элемент меню почта'''
        self.btn_email = self.wait_clickable(Locators.btn_email, 10)
        '''Элемент меню логин'''
        self.btn_login = self.wait_clickable(Locators.btn_login, 10)
        '''Элемент меню лиц. счет'''
        self.btn_ls = self.wait_clickable(Locators.btn_ls, 10)

        '''Поля ввода логина и пароля'''
        self.username = self.wait_clickable(Locators.username_input, 10)
        self.username_placeholder = self.wait_visible(Locators.username_placeholder, 10)
        self.userpass = self.wait_clickable(Locators.userpass_input, 10)

        '''Кнопка вход'''
        self.btn_submit = self.wait_clickable(Locators.btn_submit, 10)

        '''Кнопка Забыл пароль'''
        self.btn_forgot_pass = self.wait_clickable(Locators.btn_forgot_pass, 10)



