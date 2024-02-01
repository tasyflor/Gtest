from pages.home_page import MainPage


class Base:

    def right_button(self, home_page):
        text = home_page.get_virtual_servers_button().text

        assert text == 'Virtual servers'

    def check_prises(self):
        home_page = MainPage(self.driver)
        min_prise_detected = home_page.get_price_low().get_attribute('placeholder')
        home_page.get_price_high().clear()
        home_page.get_price_high().send_keys(min_prise_detected)
        prises = home_page.get_prices_from_filter()

        for prise in prises:
            value = prise.text
            filter_result = float(min_prise_detected) <= float(value) <= float(min_prise_detected) + 1
            assert filter_result

    def check_currency(self, value):
        home_page = MainPage(self.driver)
        currencies = home_page.get_currency()

        for currency in currencies:
            result = currency.text

            if value == '€':
                assert value == result
            elif value == '$':
                assert value == result
