# HisaApi
This is unofficial API for accessing current stock prices converted to Euros.
It us under development and thus further details will follow.

### Usage example

```python
from hisaapi import HisaApi
price = hisaapi.get_current_price_euro(stock='AAPL', country='United states')
```

### Status
* [![Build Status](https://github.com/hassansalehe/hisaapi/actions/workflows/ci.yml/badge.svg)](https://github.com/hassansalehe/hisaapi/actions?query=workflow%3Aci)
* [![codecov](https://codecov.io/gh/hassansalehe/hisaapi/branch/master/graph/badge.svg?token=P67YW4H678)](https://codecov.io/gh/hassansalehe/hisaapi)
