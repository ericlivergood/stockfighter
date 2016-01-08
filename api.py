import requests
import json
from collections import namedtuple

api_key = '0e13c080e89a1b1a34295c066455217880b068e2'

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


headers = {
	'X-Starfighter-Authorization' : api_key
}


def buy(account, venue, symbol, price, qty):
	url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/orders' % locals()
	order = {
		'account' : account,
		'venue': venue,
		'symbol': symbol,
		'price': price,
		'qty': qty,
		'direction': 'buy',
		'orderType': 'limit'
	}

	return json2obj(requests.post(url, data=json.dumps(order), headers=headers).text)


def sell(account, venue, symbol, price, qty):
	url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/orders' % locals()
	order = {
		'account' : account,
		'venue': venue,
		'symbol': symbol,
		'price': price,
		'qty': qty,
		'direction': 'sell',
		'orderType': 'limit'
	}

	return json2obj(requests.post(url, data=json.dumps(order), headers=headers).text)

def get_order(id):
	url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/orders/%(orderid)s' % locals()
	return json2obj(requests.get(url, headers=headers))


def get_quote(venue, symbol):
	url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/quote' % locals()
	return json2obj(requests.get(url, headers=headers).text)


def cancel_order(venue, symbol, id):
	url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/orders/%(id)s' % locals()
	return json2obj(requests.delete(url, headers=headers).text)