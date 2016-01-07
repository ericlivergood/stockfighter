import requests
import json
import time

api_key = '0e13c080e89a1b1a34295c066455217880b068e2'
venue = 'YQXJEX'
symbol = 'WSCM'
account = 'WTB87091520'


order = {
	'account' : account,
	'venue': venue,
	'symbol': symbol,
	'price': 7100,
	'qty': 100,
	'direction': 'buy',
	'orderType': 'limit'
}

url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/orders' % locals()

headers = {
	'X-Starfighter-Authorization' : api_key
}

r = requests.post(url, data=json.dumps(order), headers=headers)
order = json.loads(r.text)
orderid = order['id']

status_url = 'https://api.stockfighter.io/ob/api/venues/%(venue)s/stocks/%(symbol)s/orders/%(orderid)s' % locals()
s = requests.get(status_url, headers=headers).text
status = json.loads(s)

while(status['open']):
	status = json.loads(requests.get(status_url, headers=headers).text)
	print 'Filled ' + str(status['totalFilled'])
	time.sleep(1)

print('Complete')



