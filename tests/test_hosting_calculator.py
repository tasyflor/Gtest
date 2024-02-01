import pytest
from pages.home_page import MainPage


@pytest.mark.usefixtures('setup')
class TestBase:

    def check_prises(self):
        home_page = MainPage(self.driver)
        min_prise_detected = home_page.get_price_low().get_attribute('placeholder')
        max_prise_detected = home_page.get_price_high().get_attribute('placeholder')
        min_prise=int(min_prise_detected)+10
        max_prise=int(max_prise_detected)-10
        home_page.get_price_high().clear()
        home_page.get_price_high().send_keys(max_prise)
        home_page.get_price_low().clear()
        home_page.get_price_low().send_keys(min_prise)
        try:
            home_page.get_more_servers_button().click()
        except:
            pass
        prises = home_page.get_prices_from_filter()
        is_assertion_passed = True

        for prise in prises:
            value = prise.text
            result = float(min_prise) <= float(value) <= float(max_prise)
            if not result:
                is_assertion_passed = False

        return is_assertion_passed

    def check_equal_currency(self, result):
        home_page = MainPage(self.driver)
        currencies = home_page.get_currency()

        for currency in currencies:
            value = currency.text
            euro = '€'
            dollar='$'
            if result =='€':
                if value==euro:
                    return True
            elif result =='$':
                if value==dollar:
                    return True



    def test_virtual_euro(self):
        filter_results = self.check_prises()
        currency_result = self.check_equal_currency('€')

        assert filter_results
        assert currency_result


    def test_virtual_dollar(self):
        home_page = MainPage(self.driver)
        home_page.get_usd_button().click()
        filter_results = self.check_prises()
        currency_result = self.check_equal_currency('$')

        assert filter_results
        assert currency_result

    def test_dedicated_dollar(self):
        home_page = MainPage(self.driver)
        home_page.get_dedicated_button().click()
        home_page.get_usd_button().click()
        filter_results = self.check_prises()
        currency_result = self.check_equal_currency('$')

        assert filter_results
        assert currency_result

    def test_dedicated_euro(self):
        home_page = MainPage(self.driver)
        home_page.get_dedicated_button().click()
        filter_results = self.check_prises()
        currency_result = self.check_equal_currency('€')

        assert filter_results
        assert currency_result
