

from locators import MainPage
from data import TestData


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        # Переход в "Соусы"
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_sauces_button).click()

        sauces_button = driver.find_element(*MainPage.mn_sauces_button)
        assert 'tab_tab_type_current__2BEPc' in sauces_button.get_attribute('class'), "Таб 'Соусы' не активен"

        # Дополнительно проверяем, что заголовок соответствует ожидаемому
        h_sauce = driver.find_element(*MainPage.mn_h_sauces)
        assert h_sauce.text == TestData.SAUCES_HEADER, "Заголовок не соответствует ожидаемому"

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        # Переход в "Начинки"
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        filling_button = driver.find_element(*MainPage.mn_filling_button)

        assert 'tab_tab_type_current__2BEPc' in filling_button.get_attribute('class'), "Таб 'Начинки' не активен"

        # Дополнительно проверяем, что заголовок соответствует ожидаемому
        h_filling = driver.find_element(*MainPage.mn_h_filling)
        assert h_filling.text == TestData.FILLING_HEADER, "Заголовок не соответствует ожидаемому"

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        # Переход в "Булки"
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        driver.find_element(*MainPage.mn_ban_button).click()

        bun_button = driver.find_element(*MainPage.mn_ban_button)
        assert 'tab_tab_type_current__2BEPc' in bun_button.get_attribute('class'), "Таб 'Булки' не активен"

        # Дополнительно проверяем, что заголовок соответствует ожидаемому
        h_ban = driver.find_element(*MainPage.mn_h_ban)
        assert h_ban.text == TestData.BUN_HEADER, "Заголовок не соответствует ожидаемому"

