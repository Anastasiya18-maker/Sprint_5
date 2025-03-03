import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random



from urls import Urls
from data import ValidData

from locators import AuthRegistre, AuthLogin


class TestStellarBurgersRegistration:

    def test_registration_correct_email_and_pwd_successful_registration(self, driver):
        # успешная регистрация и переход на страницу входа


        driver.get(Urls.url_register)

        user_name =
        login = driver.find_element(Helper.generate_email())

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('s')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(s)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(f)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(AuthLogin.al_element_with_login_text))

        login_button = driver.find_element(*AuthLogin.al_element_with_login_text)

        assert driver.current_url == Urls.url_login and login_button.text == 'Вход'
    def test_registration_empty_name_nothing_happens(self, driver):
        # При пустом поле "Имя" ничего не происходит
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AuthRegistre.ar_register_button))


        errors_messages = driver.find_elements(*AuthRegistre.ar_error_message)

        assert driver.current_url == Urls.url_register and len(errors_messages) == 0

    @pytest.mark.parametrize('email_list', ['test@yaru', 'test1ya.ru', 'te st2@ya.ru', 'test3@ya .ru',
                                            '@ya.ru', 'test5@.ru', 'test6@ya.'])
    def test_registration_incorrect_email_show_error(self, driver, email_list):
        # При некорректном email ошибка, что пользователь уже есть
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys(ValidData.user_name)
        driver.find_element(*AuthRegistre.ar_email_field).send_keys(ValidData.login)
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(ValidData.password)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistre.ar_error_message_2))
        error_message = driver.find_element(*AuthRegistre.ar_error_message_2)

        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        # При вводе некорректного пароля,'Некорректный пароль'
        driver.get(Urls.url_register)

        driver.find_element(*AuthRegistre.ar_name_field).send_keys('Анастасия')
        driver.find_element(*AuthRegistre.ar_email_field).send_keys('test1@ya.ru')
        driver.find_element(*AuthRegistre.ar_password_field).send_keys(password_list)

        driver.find_element(*AuthRegistre.ar_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistre.ar_error_message))
        error_message = driver.find_element(*AuthRegistre.ar_error_message)

        assert error_message.text == 'Некорректный пароль'
