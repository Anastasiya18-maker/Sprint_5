

from locators import MainPage


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        # Переход в "Соусы"
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_sauces_button).click()

        h_sauce = driver.find_element(*MainPage.mn_h_sauces)

        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        # Переход в "Начинки"
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        h_filling = driver.find_element(*MainPage.mn_h_filling)

        assert h_filling.text == 'Начинки'

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        # Переход в "Булки"
        driver = login

        driver.find_element(*MainPage.mn_constructor_button).click()
        driver.find_element(*MainPage.mn_filling_button).click()
        driver.find_element(*MainPage.mn_ban_button).click()

        h_ban = driver.find_element(*MainPage.mn_h_ban)

        assert h_ban.text == 'Булки'

