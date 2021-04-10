from unittest.mock import patch
from unittest import TestCase
from hisaapi import HisaApi

class TestHisaApi(TestCase):

    @patch('investpy.get_stock_recent_data')
    def test_conversion_usd_to_euro(self, investpy_get):
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

        price = HisaApi.get_current_price_euro(stock='AAPL', country='United states')
        self.assertAlmostEqual(price, 102)


if __name__ == '__main__':
    unittest.main()
