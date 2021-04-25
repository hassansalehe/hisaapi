'''Unit tests for checking functionality of  hisaapi'''

import json
import unittest
from unittest.mock import patch
from unittest import TestCase

from hisaapi import HisaApi

class TestHisaApi(TestCase):
    '''
    Class holding unittests
    '''

    @patch('investpy.get_currency_cross_recent_data')
    @patch('investpy.get_stock_recent_data')
    def test_conversion_usd_to_euro(self, investpy_get_price, investpy_get_cross):
        '''
        Check that price in EUR is return for a USD stock
        '''
        test_data = {"name": "Apple",
                     "recent": [{
                         "date": "09/04/2021",
                         "open": 129.98,
                         "high": 133.0,
                         "low": 129.54,
                         "close": 133.0,
                         "volume": 106686704,
                         "currency": "USD"}]
                     }
        investpy_get_price.return_value = json.dumps(test_data)

        conversion_data = {"name": "EUR/USD",
                           "recent": [{
                               "date": "09/04/2021",
                               "open": 1.1913,
                               "high": 1.1921,
                               "low": 1.1867,
                               "close": 1.1896,
                               "currency": "USD"}]
                           }
        investpy_get_cross.return_value = json.dumps(conversion_data)

        exp_price_eur = 111.80
        hisaapi = HisaApi()
        act_price_eur = hisaapi.get_current_price_euro(stock='AAPL', country='United states')
        self.assertAlmostEqual(exp_price_eur, act_price_eur)

    @patch('investpy.get_stock_recent_data')
    def test_requesting_share_price_already_euro(self, investpy_get_price):
        '''
        Check that price in EUR is return for an EUR stock
        '''
        test_data = {"name": "Tomtom",
                     "recent": [{
                         "date": "25/04/2021",
                         "open": 7.73,
                         "high": 7.89,
                         "low": 7.73,
                         "close": 7.88,
                         "volume": 215433,
                         "currency": "EUR"}]
                     }
        investpy_get_price.return_value = json.dumps(test_data)

        exp_price_eur = 7.88
        hisaapi = HisaApi()
        act_price_eur = hisaapi.get_current_price_euro(stock='TOM2', country='Netherlands')
        self.assertAlmostEqual(exp_price_eur, act_price_eur)

if __name__ == '__main__':
    unittest.main()
