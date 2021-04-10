import investpy
import json

class HisaApi:
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
        unit = self._get_currency(stock, country)
        if 'EUR' in unit:
            return price

        cross = investpy.get_currency_cross_recent_data(currency_cross='EUR/{}'.format(unit), order='descending', as_json=True)
        per_euro = json.loads( cross )['recent'][0]['close']
        return price / float(per_euro)

    def _get_currency(self, stock, country):
        data = investpy.get_stock_recent_data(stock=stock, country=country, order='descending', as_json=True)
        return json.loads( data )['recent'][0]['currency']
