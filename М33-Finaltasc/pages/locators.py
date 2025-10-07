from selenium.webdriver.common.by import By

class Locators:

    '''Кнопка "Войти со своим паролем" для перехода на страницу авторизации'''
    standard_auth_btn = (By.ID, "standard_auth_btn")

    '''Заголовок Авторизация'''
    header_card_title = (By.ID, "card-title")

    '''Лого, заголовок, доп инфо ростелеком (Инф. материалы)'''
    logo = (By.XPATH, "//*[@id='page-left']/div/div[1]")
    rt_info_title = (By.XPATH, "//*[@id='page-left']/div/div[2]/h2")
    rt_info_text = (By.XPATH, "//*[@id='page-left']/div/div[2]/p")


    '''Поле ввода телефона, логина, почты, ЛС'''
    username_input = (By.ID, "username")
    userpass_input = (By.ID, "password")

    '''Кнопки Элементы меню: Телефон, почта, логин, ЛС'''
    username_placeholder = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/div/span")

    '''Меню выбора способа аутентификации'''
    btn_phone = (By.XPATH, "//*[@id='t-btn-tab-phone']")
    btn_email = (By.XPATH, "//*[@id='t-btn-tab-mail']")
    btn_login = (By.XPATH, "//*[@id='t-btn-tab-login']")
    btn_ls = (By.XPATH, "//*[@id='t-btn-tab-ls']")

    '''Кнопка вход'''
    btn_submit = (By.ID, "kc-login")

    btn_lk = (By.XPATH, "//*[@id='lk-btn']/span")

    '''Кнопка забыл пароль'''
    btn_forgot_pass = (By.ID, "forgot_password")

    '''Инф. сообщение "Неверный логин или пароль"'''
    form_error_message = (By.ID, "form-error-message")




