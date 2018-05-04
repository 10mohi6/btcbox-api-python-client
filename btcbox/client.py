# coding: utf-8
import hashlib
import requests
import time
import urllib
import hmac
import json
from collections import OrderedDict

class ClientError(Exception):
	pass

class Clinet(object):

	def __init__(self, **kwargs):
		self.origin = kwargs.get('origin', 'https://www.btcbox.co.jp')
		public_key = kwargs.get('public_key', None)
		if public_key is None:
			raise ClientError('public key is absent.')
		self.public_key = public_key
		private_key = kwargs.get('private_key', None)
		if private_key is None:
			raise ClientError('private key is absent.')
		self.private_key = private_key

	def _request(self, path, method='GET', headers=None, params=None):
		uri = '{0}{1}'.format(self.origin, path)
		if method == 'GET':
			res = requests.get(uri, headers=headers, params=params)
		elif method == 'POST':
			res = requests.post(uri, headers=headers, data=params)
		else:
			message = '{0} is not supported.'.format(method)
			raise NotImplementedError(message)

		if res.status_code != 200:
			message = '{0} {1} failed: {2}'.format(method, uri, res.status_code)
			raise ClientError(message)

		data = json.loads(res.content)

		return data

	def _signature(self, params):
		payload = bytearray(urllib.parse.urlencode(params),'ASCII')
		md5prikey = bytearray(hashlib.md5(self.private_key.encode('utf-8')).hexdigest(),'ASCII')
		sign = urllib.parse.quote(hmac.new(md5prikey, payload, hashlib.sha256).hexdigest())
		return sign

	def ticker(self, **kwargs):
		path = '/api/v1/ticker'
		params = OrderedDict()
		params['coin'] = kwargs.get('coin', 'btc')

		data = self._request(path, params=params)

		return data

	def depth(self):
		path = '/api/v1/depth'
		params = None

		data = self._request(path, params=params)

		return data

	def orders(self):
		path = '/api/v1/orders'
		params = None

		data = self._request(path, params=params)

		return data

	def balance(self, **kwargs):
		path = '/api/v1/balance'
		params = OrderedDict()
		params['key'] = self.public_key
		params['coin'] = kwargs.get('coin', 'btc')
		params['nonce'] = time.time()
		params['signature'] = self._signature(params)

		data = self._request(path, method='POST', params=params)

		return data
	
	def wallet(self, **kwargs):
		path = '/api/v1/wallet'
		params = OrderedDict()
		params['coin'] = kwargs.get('coin', 'btc')
		params['key'] = self.public_key
		params['nonce'] = time.time()
		params['signature'] = self._signature(params)

		data = self._request(path, method='POST', params=params)

		return data

	def trade_list(self, **kwargs):
		path = '/api/v1/trade_list'
		params = OrderedDict()
		params['coin'] = kwargs.get('coin', 'btc')
		params['key'] = self.public_key
		params['nonce'] = time.time()
		params['since'] = kwargs.get('since', 0)
		type = kwargs.get('type', None)
		if type is None:
			raise ClientError('type is absent.')
		params['type'] = type
		params['signature'] = self._signature(params)

		data = self._request(path, method='POST', params=params)

		return data

	def trade_view(self, **kwargs):
		path = '/api/v1/trade_view'
		params = OrderedDict()
		params['coin'] = kwargs.get('coin', 'btc')
		params['key'] = self.public_key
		params['nonce'] = time.time()
		id = kwargs.get('id', None)
		if id is None:
			raise ClientError('id is absent.')
		params['id'] = id
		params['signature'] = self._signature(params)

		data = self._request(path, method='POST', params=params)

		return data

	def trade_cancel(self, **kwargs):
		path = '/api/v1/trade_cancel'
		params = OrderedDict()
		params['coin'] = kwargs.get('coin', 'btc')
		params['key'] = self.public_key
		params['nonce'] = time.time()
		id = kwargs.get('id', None)
		if id is None:
			raise ClientError('id is absent.')
		params['id'] = id
		params['signature'] = self._signature(params)

		data = self._request(path, method='POST', params=params)

		return data

	def trade_add(self, **kwargs):
		path = '/api/v1/trade_add'
		params = OrderedDict()
		params['coin'] = kwargs.get('coin', 'btc')
		params['key'] = self.public_key
		params['nonce'] = time.time()
		amount = kwargs.get('amount', None)
		if amount is None:
			raise ClientError('amount is absent.')
		params['amount'] = amount
		price = kwargs.get('price', None)
		if price is None:
			raise ClientError('price is absent.')
		params['price'] = price
		type = kwargs.get('type', None)
		if type is None:
			raise ClientError('type is absent.')
		params['type'] = type
		params['signature'] = self._signature(params)

		data = self._request(path, method='POST', params=params)

		return data
