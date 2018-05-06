# coding: utf-8
import hashlib
import requests
import time
import urllib
import hmac


class Client(object):

	def __init__(self, **kwargs):
		self.origin = kwargs.get('origin', 'https://www.btcbox.co.jp')
		self.public_key = kwargs.get('public_key', None)
		if self.public_key is None:
			raise Exception('public key is absent.')
		self.private_key = kwargs.get('private_key', None)
		if self.private_key is None:
			raise Exception('private key is absent.')
		self.timeout = kwargs.get('timeout', None)

	def _request(self, path, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		params['key'] = self.public_key
		params['nonce'] = time.time()
		params['signature'] = self._signature(params)
		if method == 'GET':
			res = requests.get(uri, timeout=self.timeout, params=params)
		else: # method == 'POST'
			res = requests.post(uri, timeout=self.timeout, data=params)

		return res

	def _signature(self, params):
		payload = bytearray(urllib.parse.urlencode(params),'ASCII')
		md5prikey = bytearray(hashlib.md5(self.private_key.encode('utf-8')).hexdigest(),'ASCII')
		sign = urllib.parse.quote(hmac.new(md5prikey, payload, hashlib.sha256).hexdigest())
		return sign

	def ticker(self, **kwargs):
		path = '/api/v1/ticker'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def depth(self, **kwargs):
		path = '/api/v1/depth'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def orders(self, **kwargs):
		path = '/api/v1/orders'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def balance(self, **kwargs):
		path = '/api/v1/balance'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data
	
	def wallet(self, **kwargs):
		path = '/api/v1/wallet'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def trade_list(self, **kwargs):
		path = '/api/v1/trade_list'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def trade_view(self, **kwargs):
		path = '/api/v1/trade_view'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def trade_cancel(self, **kwargs):
		path = '/api/v1/trade_cancel'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def trade_add(self, **kwargs):
		path = '/api/v1/trade_add'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data
