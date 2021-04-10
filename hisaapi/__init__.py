'''API for retrieving current price of a stock in Euro currency '''

import investpy
import json

class HisaApi:
    '''
    Class holding public API
    '''

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

        data = investpy.get_stock_recent_data(stock=stock, country=country, order='descending', as_json=True)
        price = json.loads( data )['recent'][0]['close']
        unit = json.loads( data )['recent'][0]['currency']
        if 'EUR' in unit:
            return price

        cross = investpy.get_currency_cross_recent_data(currency_cross='EUR/{}'.format(unit), order='descending', as_json=True)
        per_euro = json.loads( cross )['recent'][0]['close']
        return round(price / float(per_euro), 2)
