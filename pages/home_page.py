from base.selenium_base import SeleniumBase


class MainPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_dedicated_servers = '//button[contains(text(), "Dedicated servers")]'
        self.__xpath_price_low = '(//input[contains(@type, \'number\')])[1]'
        self.__xpath_price_high = '(//input[contains(@type, \'number\')])[2]'
        self.__xpath_usd = '//input[@value=\'USD\']'
        self.__xpath_eur = '//input[@value=\'EUR\']'
        self.__xpath_prices_filter = '//div[contains(@class, \'price-card_price\')]//span'
        self.__xpath_check_currency = '//div[contains(@class, \'price-card_price\')]//descendant::sub[1]'
        self.__xpath_more_servers_button = '//div[contains(text(),  "Show more")]'

    def get_dedicated_button(self):
        return self.is_present('xpath', self.__xpath_dedicated_servers, 'Dedicated servers button')

    def get_usd_button(self):
        return self.is_present('xpath', self.__xpath_usd, 'Usd button')

    def get_eur_button(self):
        return self.is_present('xpath', self.__xpath_eur, 'Eur button')

    def get_price_low(self):
        return self.is_present('xpath', self.__xpath_price_low, 'Min price')

    def get_price_high(self):
        return self.is_present('xpath', self.__xpath_price_high, 'Max price')

    def get_prices_from_filter(self):
        return self.are_visible('xpath', self.__xpath_prices_filter, 'All prices filter')

    def get_currency(self):
        return self.are_visible('xpath', self.__xpath_check_currency, 'Currency check')

    def get_more_servers_button(self):
        return self.is_present('xpath', self.__xpath_more_servers_button, 'More servers button')