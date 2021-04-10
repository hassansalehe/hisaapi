'''Unit tests for checking functionality of  hisaapi'''

import unittest
from unittest.mock import patch
from unittest import TestCase
from hisaapi import HisaApi

class TestHisaApi(TestCase):
    '''
    Class holding unittests
    '''

    @patch('investpy.get_stock_recent_data')
    def test_conversion_usd_to_euro(self, investpy_get):
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

        investpy_get.return_value = test_data

        exp_price_eur = 117.76
        hisaapi = HisaApi()
        act_price_eur = hisaapi.get_current_price_euro(stock='AAPL', country='United states')
        self.assertAlmostEqual(exp_price_eur, act_price_eur)


if __name__ == '__main__':
    unittest.main()
