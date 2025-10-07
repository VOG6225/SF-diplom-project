import pytest
from config import *

import time
from selenium.webdriver.common.keys import Keys

from pages.auth_page import *



class TestAuthPage:
    """ТК 001 - Проверка наполнения страницы Авторизации"""
    def test_auth_page_info(self, driver):
        page = AuthPage(driver)

        assert page.authorization.text == auth_header
        print("\nТест № 1 - ТК-001 - Проверка 1.1 - Страница авторизации доступна")
        assert page.logo.is_displayed()
        print("Тест № 1 - ТК-001 - Проверка 1.2 - Лого отображается")
        assert page.rt_info_title.text == auth_info_title
        print("Тест № 1 - ТК-001 - Проверка 1.3 - Заголовок логотипа отображается")
        assert page.rt_info_text.text == auth_info_text
        print("Тест № 1 - ТК-001 - Проверка 1.4 - Заголовок логотипа отображается")

    '''TK 002 проверка меню выбора типа аутентификации '''
    def test_auth_page_menu(self, driver):
        page = AuthPage(driver)
        color = page.btn_phone.value_of_css_property('color')

        btn_email = page.btn_email
        btn_login = page.btn_login
        btn_ls = page.btn_ls
        btn_phone = page.btn_phone

        username = page.username    # Поле ввода логин
        userpass = page.userpass    # Поле ввода пароль

        username_placeholder = page.username_placeholder # Текст подсказка поля логин


        '''Проверка активной кнопки Телефон'''
        assert color == orang_rgba
        assert username_placeholder.text == 'Мобильный телефон'
        print("\nТест № 2 - ТК-002 - Проверка 1.1 - Кнопка телефон имеется, активна по умолчанию, цвет оранжевый, поле подсказка: Мобильный телефон")

        '''Проверка кнопки Почта'''
        btn_email.click()
        assert btn_email.value_of_css_property('color') ==orang_rgba
        assert username_placeholder.text == 'Электронная почта'
        print("Тест № 3 - ТК-002 - Проверка 1.2 - Кнопка почта имеется, кликабельна, при нажатии цвет оранжевый, поле подсказка: Электронная почта")

        '''Проверка кнопки Логин'''
        btn_login.click()
        assert btn_login.value_of_css_property('color') ==orang_rgba
        assert username_placeholder.text == 'Логин'
        print("Тест № 4 - ТК-002 - Проверка 1.3 - Кнопка логин имеется, кликабельна, при нажатии цвет оранжевый, поле подсказка: Логин")

        '''Проверка кнопки Лицевой счет'''
        btn_ls.click()
        assert btn_ls.value_of_css_property('color') ==orang_rgba
        assert username_placeholder.text == 'Лицевой счёт'
        print("Тест № 5 - ТК-002 - Проверка 1.4 - Кнопка лицевой счет имеется, кликабельна, при нажатии цвет оранжевый, поле подсказка: Лицевой счет")



    '''TK 003 проверка наличия и функциональности поля ввода пароля'''
    def test_password_input_functionality(self, driver):
        page = AuthPage(driver)

        userpass = page.userpass
        userpass.click()
        userpass.send_keys(auth_password)

        assert userpass.is_displayed()
        assert userpass.get_attribute('value') == auth_password
        print("\nТест № 6 - ТК-003 - Проверка 1.1 - Поле ввода пароля имеется, позволяет вводить данные")

    '''ТК 004 проверка автоматической смены таба вида авторизации на "Почта" при вводе адреса электронной почты.'''
    def test_auto_switch_to_email_tab(self, driver):

        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_email = page.btn_email
        username = page.username
        userpass = page.userpass

        assert btn_phone.value_of_css_property('color') == orang_rgba
        username.click()
        username.send_keys(auth_email)
        userpass.click()
        assert btn_email.value_of_css_property('color') == orang_rgba, "\nТест № 7 - ТК-004 - Проверка 1.1 ПРОВАЛЕН: Таб не переключился на почту"
        print("\nТест № 7 - ТК-004 - Проверка 1.1 - При вводе в поле логина адреса эл. почты, \n"
                  "происходит автоматическая смена способа аутентификации на Почта, \n"
                  "таб становится активным, цвет таба - оранжевый")




    '''ТК 005 проверка автоматической смены таба вида авторизации на "Логин" при вводе логина.'''

    def test_auto_switch_to_login_tab(self, driver):

        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_login = page.btn_login
        username = page.username
        userpass = page.userpass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        username.click()
        username.send_keys(auth_login)
        userpass.click()
        assert btn_login.value_of_css_property('color') == orang_rgba, "\nТест № 8 - ТК-005 - Проверка 1.1 ПРОВАЛЕН: Таб не переключился на Логин"
        print("\nТест № 8 - ТК-005 - Проверка 1.1 - При вводе в поле логин тестового логина, \n"
                  "происходит автоматическая смена способа аутентификации на Логин, \n"
                  "таб становится активным, цвет таба - оранжевый")

    '''ТК 006 проверка автоматической смены таба вида авторизации на "Личевой счет" при вводе номера лицевого счета.'''

    def test_auto_switch_to_ls_tab(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_ls = page.btn_ls
        username = page.username
        userpass = page.userpass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        username.click()
        username.send_keys(auth_ls)
        userpass.click()
        assert btn_ls.value_of_css_property('color') == orang_rgba, "\nТест № 9 - ТК-006 - Проверка 1.1 ПРОВАЛЕН: Таб не переключился на Лицевой счет"
        print("\nТест № 9 - ТК-006 - Проверка 1.1 - При вводе в поле логин тестового номера лицевого счета, \n"
              "происходит автоматическая смена способа аутентификации на Лицевой счет, \n"
              "таб становится активным, цвет таба - оранжевый")

    '''ТК 007 проверка автоматической смены таба вида авторизации на "Телефон" при вводе номера телефона.'''

    def test_auto_switch_to_phone_tab(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_login = page.btn_login
        username = page.username
        userpass = page.userpass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        btn_login.click()
        assert btn_login.value_of_css_property('color') == orang_rgba
        username.click()
        username.send_keys(auth_phone)
        userpass.click()
        assert btn_phone.value_of_css_property('color') == orang_rgba, "\nТест № 10 - ТК-007 - Проверка 1.1 ПРОВАЛЕН: Таб не переключился на Телефон"
        print("\nТест № 10 - ТК-007 - Проверка 1.1 - При вводе в поле логин тестового номера телефона, \n"
              "происходит автоматическая смена способа аутентификации на Телефон, \n"
              "таб становится активным, цвет таба - оранжевый")


    ''' ТК 008 - Проверка авторизаии клиента по номеру телефона с корректной парой логин пароль'''

    def test_valid_auth(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit


        assert btn_phone.value_of_css_property('color') == orang_rgba
        username.click()
        username.send_keys(valid_phone)
        userpass.click()
        userpass.send_keys(valid_password)
        btn_submit.click()

        btn_lk = page.wait_clickable(Locators.btn_lk, 10)
        btn_lk.click()

        current_url = driver.current_url
        assert current_url == lk_rt_url, "\nТест № 11 - ТК-008 - Проверка 1.1 ПРОВАЛЕН: Пользователь не прошел авторизацию с валидными данными"
        print("\nТест № 11 - ТК-008 - Проверка 1.1 - Пользователь успешно авторизовался с валидными данными, \n"
                   "Осуществлен переход в ЛК абонента  \n")

    ''' ТК 009 - Проверка авторизаии клиента по номеру телефона: введен только телефон'''

    def test_auth_no_pass(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba
        username.click()
        username.send_keys(valid_phone)
        current_url = driver.current_url
        btn_submit.click()

        assert current_url == driver.current_url, "Тест № 12 - ТК-009 - Проверка 1.1 - Проверка провалена, осуществлен переход с страницы авторизации"
        print("\nТест № 12 - ТК-009 - Проверка 1.1 - Пользователь не авторизован, активна страница регистрации \n")


    ''' ТК 010 - Проверка авторизации клиента по номеру телефона: Введен только пароль'''

    def test_auth_no_phone(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba
        userpass.click()
        userpass.send_keys(valid_password)
        current_url = driver.current_url
        btn_submit.click()

        assert current_url == driver.current_url, "Тест № 13 - ТК-010 - Проверка 1.1 Проверка провалена, осуществлен переход с страницы авторизации"
        print("\nТест № 13 - ТК-010 - Проверка 1.1 - Пользователь не авторизован, активна страница регистрации \n")


    ''' ТК 011 - Проверка авторизации клиента по номеру телефона: Введен не корректный номер'''

    def test_auth_no_valid_phone1(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit
        btn_forgot_pass = page.btn_forgot_pass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        assert btn_forgot_pass.value_of_css_property('color') != orang_rgba, "Проверка провалена, цвет кнопки Забыл пароль, изначально оранжевый"

        username.send_keys(auth_phone)
        userpass.send_keys(valid_password)

        btn_submit.click()
        btn_forgot_pass = page.wait_clickable(Locators.btn_forgot_pass, 10)
        assert btn_forgot_pass.value_of_css_property('color') == orang_rgba, "Тест № 14 - ТК-011 - Проверка 1.1 Проверка провалена, цвет кнопки Забыл пароль, не оранжевый"
        print("\nТест № 14 - ТК-011 - Проверка 1.1 - Пользователь не авторизован, кнопка Забыл пароль, изменила цвет на оранжевый \n")

    ''' ТК 011 - Проверка авторизации клиента по номеру телефона: Введен не корректный номер'''
    def test_auth_no_valid_phone2(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(valid_phone)
        userpass.send_keys(auth_password)
        btn_submit.click()
        form_error_message = page.wait_visible(Locators.form_error_message, 10)

        assert form_error_message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки", "Тест № 15 - ТК-011 - Проверка 1.2 Проверка провалена, информационное сообщение об ошибке отсутствует"
        print("\nТест № 15 - ТК-011 - Проверка 1.2 - Пользователь не авторизован, появилось сообщение об ошибке: Неверный логин или пароль  \n")


    ''' ТК 012 - Проверка авторизации клиента по номеру телефона: Введен не корректный пароль'''

    def test_auth_no_valid_pass1(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit
        btn_forgot_pass = page.btn_forgot_pass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        assert btn_forgot_pass.value_of_css_property('color') != orang_rgba, "Проверка провалена, цвет кнопки Забыл пароль, изначально оранжевый"

        username.send_keys(valid_phone)
        userpass.send_keys(auth_password)

        btn_submit.click()
        btn_forgot_pass = page.wait_clickable(Locators.btn_forgot_pass, 10)
        assert btn_forgot_pass.value_of_css_property('color') == orang_rgba, "Тест № 16 - ТК-012 - Проверка 1.1 - Проверка провалена, цвет кнопки Забыл пароль, не оранжевый"
        print("\nТест № 16 - ТК-012 - Проверка 1.1 - Пользователь не авторизован, кнопка Забыл пароль, изменила цвет на оранжевый \n")

    ''' ТК 012 - Проверка авторизации клиента по номеру телефона: Введен не корректный пароль'''

    def test_auth_no_valid_pass2(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(valid_phone)
        userpass.send_keys(auth_password)
        btn_submit.click()
        form_error_message = page.wait_visible(Locators.form_error_message, 10)

        assert form_error_message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки", "Тест № 17 - ТК-012 - Проверка 1.2 - Проверка провалена, информационное сообщение об ошибке отсутствует"
        print("\nТест № 17 - ТК-012 - Проверка 1.2 - Пользователь не авторизован, появилось сообщение об ошибке: Неверный логин или пароль  \n")



    ''' ТК 013 - Проверка авторизации клиента по email с корректной парой почта пароль'''

    def test_valid_auth_email(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_email = page.btn_email
        btn_submit = page.btn_submit
        username = page.username
        userpass = page.userpass

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(valid_email)
        userpass.click()
        assert btn_email.value_of_css_property('color') == orang_rgba
        userpass.send_keys(valid_password)
        btn_submit.click()

        btn_lk = page.wait_clickable(Locators.btn_lk, 10)
        btn_lk.click()

        current_url = driver.current_url
        assert current_url == lk_rt_url, "\nТест № 18 - ТК-013 - Проверка 1.1 - Пользователь не прошел авторизацию с валидными данными"
        print("\nТест № 18 - ТК-013 - Проверка 1.1 - Пользователь успешно авторизовался с валидными данными, \n"
                       "Осуществлен переход в ЛК абонента  \n")

    ''' ТК 014 - Проверка авторизации клиента по email введен не корректный email (цвет кнопки)'''


    def test_auth_no_valid_email1(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_email = page.btn_email
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit
        btn_forgot_pass = page.btn_forgot_pass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        assert btn_forgot_pass.value_of_css_property('color') != orang_rgba, "Тест № 19 - ТК-014 - Проверка 1.1 - Проверка провалена, цвет кнопки Забыл пароль, изначально оранжевый"

        username.send_keys(auth_email)
        userpass.send_keys(valid_password)

        assert btn_email.value_of_css_property('color') == orang_rgba

        btn_submit.click()
        btn_forgot_pass = page.wait_clickable(Locators.btn_forgot_pass, 10)
        assert btn_forgot_pass.value_of_css_property('color') == orang_rgba, "Тест № 19 - ТК-014 - Проверка 1.1 - Проверка провалена, цвет кнопки Забыл пароль, не оранжевый"
        print("\nТест № 19 - ТК-014 - Проверка 1.1 - Пользователь не авторизован, кнопка Забыл пароль, изменила цвет на оранжевый \n")

    ''' ТК 014 - Проверка авторизации клиента по email телефона: Введен не корректный email (Сообщение об ошибке)'''

    def test_auth_no_valid_email2(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_email = page.btn_email
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(auth_email)
        userpass.send_keys(valid_password)
        btn_submit.click()
        form_error_message = page.wait_visible(Locators.form_error_message, 10)

        assert form_error_message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки", "Тест № 20 - ТК-014 - Проверка 1.2 - Проверка провалена, информационное сообщение об ошибке отсутствует"
        print("\nТест № 20 - ТК-015 - Проверка 1.1 - Пользователь не авторизован, появилось сообщение об ошибке: Неверный логин или пароль  \n")




    ''' ТК 015 - Проверка авторизации клиента по email введен не корректный пароль (цвет кнопки)'''


    def test_auth_no_valid_email1(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_email = page.btn_email
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit
        btn_forgot_pass = page.btn_forgot_pass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        assert btn_forgot_pass.value_of_css_property('color') != orang_rgba, "Тест № 21 - ТК-014 - Проверка 1.1 - Проверка провалена, цвет кнопки Забыл пароль, изначально оранжевый"

        username.send_keys(auth_email)
        userpass.send_keys(valid_password)

        assert btn_email.value_of_css_property('color') == orang_rgba

        btn_submit.click()
        btn_forgot_pass = page.wait_clickable(Locators.btn_forgot_pass, 10)
        assert btn_forgot_pass.value_of_css_property('color') == orang_rgba, "Тест № 21 - ТК-015 - Проверка 1.2 - Проверка провалена, цвет кнопки Забыл пароль, не оранжевый"
        print("\nТест № 21 - ТК-015 - Проверка 1.2 - Пользователь не авторизован, кнопка Забыл пароль, изменила цвет на оранжевый \n")

    ''' ТК 015 - Проверка авторизации клиента по email телефона: Введен не корректный пароль (Сообщение об ошибке)'''

    def test_auth_no_valid_email2(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_email = page.btn_email
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(valid_email)
        userpass.send_keys(auth_password)
        btn_submit.click()
        form_error_message = page.wait_visible(Locators.form_error_message, 10)

        assert form_error_message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки", "Тест № 22 - ТК-015 - Проверка 1.3- Проверка провалена, информационное сообщение об ошибке отсутствует"
        print("\nТест № 22 - ТК-015 - Проверка 1.2 - Пользователь не авторизован, появилось сообщение об ошибке: Неверный логин или пароль  \n")



    ''' ТК 016 - Проверка авторизации клиента по ЛС с корректной парой  номер ЛС - пароль'''

    def test_valid_auth_ls(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_ls = page.btn_ls
        btn_submit = page.btn_submit
        username = page.username
        userpass = page.userpass

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(valid_ls)
        userpass.click()
        assert btn_ls.value_of_css_property('color') == orang_rgba
        userpass.send_keys(valid_password)
        btn_submit.click()

        btn_lk = page.wait_clickable(Locators.btn_lk, 10)
        btn_lk.click()

        current_url = driver.current_url
        assert current_url == lk_rt_url, "\nТест № 23 - ТК-016 - Проверка 1.1 - Пользователь не прошел авторизацию с валидными данными"
        print("\nТест № 23 - ТК-016 - Проверка 1.1 - Пользователь успешно авторизовался с валидными данными, \n"
                       "Осуществлен переход в ЛК абонента  \n")




    ''' ТК 017 - Проверка авторизации клиента по ЛС введен не корректный пароль (цвет кнопки)'''

    def test_auth_no_valid_ls1(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_ls = page.btn_ls
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit
        btn_forgot_pass = page.btn_forgot_pass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        assert btn_forgot_pass.value_of_css_property(
            'color') != orang_rgba, "Тест № 24 - ТК-017 - Проверка 1.1 - Проверка провалена, цвет кнопки Забыл пароль, изначально оранжевый"

        username.send_keys(valid_ls)
        userpass.send_keys(auth_password)

        assert btn_ls.value_of_css_property('color') == orang_rgba

        btn_submit.click()
        btn_forgot_pass = page.wait_clickable(Locators.btn_forgot_pass, 10)
        assert btn_forgot_pass.value_of_css_property(
            'color') == orang_rgba, "Тест № 24 - ТК-017 - Проверка 1.2 - Проверка провалена, цвет кнопки Забыл пароль, не оранжевый"
        print(
            "\nТест № 24 - ТК-017 - Проверка 1.2 - Пользователь не авторизован, кнопка Забыл пароль, изменила цвет на оранжевый \n")




    ''' ТК 017 - Проверка авторизации клиента по ЛС телефона: Введен не корректный пароль (Сообщение об ошибке)'''

    def test_auth_no_valid_ls2(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_ls = page.btn_ls
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(valid_ls)
        userpass.send_keys(auth_password)
        btn_submit.click()
        form_error_message = page.wait_visible(Locators.form_error_message, 10)

        assert form_error_message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки", "Тест № 25 - ТК-017 - Проверка 1.3- Проверка провалена, информационное сообщение об ошибке отсутствует"
        print(
            "\nТест № 25 - ТК-017 - Проверка 1.3 - Пользователь не авторизован, появилось сообщение об ошибке: Неверный логин или пароль  \n")





    ''' ТК 018 - Проверка авторизации клиента по ЛС введен не корректный номер ЛС (цвет кнопки)'''

    def test_auth_no_valid_ls1(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_ls = page.btn_ls
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit
        btn_forgot_pass = page.btn_forgot_pass
        assert btn_phone.value_of_css_property('color') == orang_rgba
        assert btn_forgot_pass.value_of_css_property(
            'color') != orang_rgba, "Тест № 25 - ТК-018 - Проверка 1.1 - Проверка провалена, цвет кнопки Забыл пароль, изначально оранжевый"

        username.send_keys(auth_ls)
        userpass.send_keys(valid_password)

        assert btn_ls.value_of_css_property('color') == orang_rgba

        btn_submit.click()
        btn_forgot_pass = page.wait_clickable(Locators.btn_forgot_pass, 10)
        assert btn_forgot_pass.value_of_css_property(
            'color') == orang_rgba, "Тест № 25 - ТК-018 - Проверка 1.2 - Проверка провалена, цвет кнопки Забыл пароль, не оранжевый"
        print(
            "\nТест № 25 - ТК-018 - Проверка 1.2 - Пользователь не авторизован, кнопка Забыл пароль, изменила цвет на оранжевый \n")




    ''' ТК 018 - Проверка авторизации клиента по ЛС телефона: Введен не корректный номер ЛС (Сообщение об ошибке)'''

    def test_auth_no_valid_ls2(self, driver):
        page = AuthPage(driver)
        btn_phone = page.btn_phone
        btn_ls = page.btn_ls
        username = page.username
        userpass = page.userpass
        btn_submit = page.btn_submit

        assert btn_phone.value_of_css_property('color') == orang_rgba

        username.send_keys(auth_ls)
        userpass.send_keys(valid_password)
        btn_submit.click()
        form_error_message = page.wait_visible(Locators.form_error_message, 10)

        assert form_error_message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки", "Тест № 26 - ТК-018 - Проверка 1.3- Проверка провалена, информационное сообщение об ошибке отсутствует"
        print(
            "\nТест № 26 - ТК-018 - Проверка 1.3 - Пользователь не авторизован, появилось сообщение об ошибке: Неверный логин или пароль  \n")