from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from urls import Urls

from locators import MainPage, LKProfile, AuthLogin
from data import Data


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login):
        # Открыть ЛК


        login.find_element(*MainPage.mn_profile_button).click()


        WebDriverWait(login, Data.WAIT_TIME).until(EC.visibility_of_element_located(LKProfile.lk_history_shop_button))
        assert Urls.url_profile == login.current_url

    def test_click_constructor_button_show_constructor_form(self, login):
        # Переход из ЛК в конструктор при нажатии кнопки 'Конструктор'


        login.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(login, Data.WAIT_TIME).until(EC.visibility_of_element_located(LKProfile.lk_history_shop_button))
        login.find_element(*MainPage.mn_constructor_button).click()

        h1_tag = login.find_elements(*MainPage.mn_h_ban)
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Булки'

    def test_click_logo_button_show_constructor_form(self, login):
        # Переход из ЛК в конструктор при нажатии на лого


        login.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(login, Data.WAIT_TIME).until(EC.visibility_of_element_located(LKProfile.lk_history_shop_button))
        login.find_element(*MainPage.mn_logo).click()

        h1_tag = login.find_elements(*MainPage.mn_h_ban)
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Булки'

    def test_click_logout_button_in_lk_open_login_form(self, login):
        # Выход из аккаунта


        login.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(login, Data.WAIT_TIME).until(EC.visibility_of_element_located(LKProfile.lk_history_shop_button))

        login.find_element(*LKProfile.lk_logout_button).click()
        WebDriverWait(login, Data.WAIT_TIME).until(EC.visibility_of_element_located(AuthLogin.al_login_button_any_forms))

        login_button = login.find_element(*AuthLogin.al_element_with_login_text)
        assert login.current_url == Urls.url_login and login_button.text == 'Вход'
