# btcbox.client

[![PyPI version](https://badge.fury.io/py/btcbox.client.svg)](https://badge.fury.io/py/btcbox.client)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

btcbox.client is a python client library for btcbox api

## Installation

    $ pip install btcbox.client

## Usage

```python
from btcbox.client import Client

client = Clinet(public_key='your public key', private_key='your private key')

#
# /api/v1/ticker
#
data = client.ticker()
print(data)
# {"high":39700,"low":36300,"buy":1.879,"sell":0,"last":38800,"vol":283.954}

#
# /api/v1/depth
#
data = client.depth()
print(data)
# {"asks":[[70000,5],[69000,0.48],[67000,0.9999],[64498,0.02],[61160,0.017],[60980,0.03],[60000,0.1924],[55900,1.4],[55100,2],[55044,0.019],[54500,0.7836],[54190,1],[52500,5.8645],[51500,5.6594],[51490,0.02],[47500,7],[45999,0.0244],[44585,0.024],[43000,10],[41700,10],[41300,6],[40900,10],[40500,6],[40125,10.0277],[40100,5],[40089,0.509],[39800,14.7132],[39799,0.0695],[39798,5],[39700,2.89],[39000,0.209]],"bids":[[38300,1.879],[38100,1.0078],[38000,1.24],[37700,4.706],[37600,3.8313],[37001,0.146],[36999,5.8],[36400,5],[36200,1.3314],[36002,2],[36000,1.568],[35501,0.282],[35500,9.9],[35200,5.6],[35010,10],[35001,0.03],[34600,7.6],[34500,5.505],[34200,9.3],[34000,6.4],[33800,4.434],[33333,3],[32830,0.0305],[31800,2],[31500,3.018],[30001,0.03],[30000,11.48],[28000,10],[25001,0.04],[22000,5.863],[20001,0.05],[460,10]]}

#
# /api/v1/orders
#
data = client.orders()
print(data)
# [{"date":"0","price":3,"amount":0.1,"tid":"1","type":"buy"},{"date":"0","price":32323,"amount":2,"tid":"2","type":"sell"},{"date":"0","price":32,"amount":432,"tid":"3","type":"sell"},{"date":"0","price":323,"amount":2,"tid":"4","type":"sell"},{"date":"0","price":2100,"amount":0.3,"tid":"5","type":"buy"}]

#
# /api/v1/balance
#
data = client.balance()
print(data)
# {"uid":8,"nameauth":0,"moflag":0,"btc_balance":4234234,"btc_lock":0,"ltc_balance":32429.6,"ltc_lock":2.4,"doge_balance":0,"doge_lock":0,"jpy_balance":2344581.519,"jpy_lock":868862.481}

#
# /api/v1/wallet
#
data = client.wallet()
print(data)
# {"result":true, "address":"1xxxxxxxxxxxxxxxxxxxxxxxx"}

#
# /api/v1/trade_list
#
data = client.trade_list(type='open')
print(data)
# [{"id":"11","datetime":"2014-10-21 10:47:20","type":"sell","price":42000,"amount_original":1.2,"amount_outstanding":1.2},{"id":"10","datetime":"2014-10-20 13:29:39","type":"sell","price":42000,"amount_original":1.2,"amount_outstanding":1.2},{"id":"9","datetime":"2014-10-20 13:29:29","type":"sell","price":42000,"amount_original":1.2,"amount_outstanding":1.2},{"id":"8","datetime":"2014-10-20 13:28:14","type":"buy","price":42800,"amount_original":0.34,"amount_outstanding":0.34},{"id":"7","datetime":"2014-10-20 13:27:38","type":"buy","price":42750,"amount_original":0.235,"amount_outstanding":0.235},{"id":"6","datetime":"2014-10-20 13:27:15","type":"buy","price":43299,"amount_original":4.789,"amount_outstanding":4.789},{"id":"5","datetime":"2014-10-20 13:26:52","type":"buy","price":42500,"amount_original":14,"amount_outstanding":14},{"id":"4","datetime":"2014-10-20 13:26:23","type":"buy","price":43200,"amount_original":0.4813,"amount_outstanding":0.4813},{"id":"3","datetime":"2014-10-20 13:25:57","type":"buy","price":43200,"amount_original":0.4813,"amount_outstanding":0.4813}]

#
# /api/v1/trade_view
#
data = client.trade_view(id=11)
print(data)
# {"id":11,"datetime":"2014-10-21 10:47:20","type":"sell","price":42000,"amount_original":1.2,"amount_outstanding":1.2,"status":"closed","trades":[]}

#
# /api/v1/trade_cancel
#
data = client.trade_cancel(id=11)
print(data)
# {"result":true, "id":"11"}

#
# /api/v1/trade_add
#
data = client.trade_add(amount=1, price=1, type='buy')
print(data)
# {"result":true, "id":"11"}
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request