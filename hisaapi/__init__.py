'''API for retrieving current price of a stock in Euro currency '''

import json
import investpy

class HisaApi:
    '''
    Class holding public API
    '''
    def __init__(self):
        self.data = {}

    def get_current_price(self, stock, country):
        '''
        Get current price of stick in original currency
        '''
        self.data = investpy.get_stock_recent_data(stock=stock, country=country,
                                                   order='descending', as_json=True)
        return json.loads(self.data)['recent'][0]['close']

    def get_current_price_euro(self, stock, country):
        '''
        Get current price of a stock in Euros.

        Parameters
        ----------
        stock: str
            The ticker of a stock
        country: str
            Country of the stock
        '''
        price = self.get_current_price(stock, country)
        unit = self._get_currency()
        if 'EUR' in unit:
            return price

        cross = investpy.get_currency_cross_recent_data(currency_cross='EUR/{}'.format(unit),
                                                        order='descending', as_json=True)
        per_euro = json.loads(cross)['recent'][0]['close']
        return round(price / float(per_euro), 2)

    def _get_currency(self):
        return json.loads(self.data)['recent'][0]['currency']
