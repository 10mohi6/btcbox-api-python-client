# coding: utf-8
import grequests
import time
from sync import Client

class Async(Client):

	def _request(self, path, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		params['key'] = self.public_key
		params['nonce'] = time.time()
		params['signature'] = self._signature(params)
		if method == 'GET':
			res = grequests.get(uri, timeout=self.timeout, params=params)
		else: # method == 'POST'
			res = grequests.post(uri, timeout=self.timeout, data=params)

		return res
