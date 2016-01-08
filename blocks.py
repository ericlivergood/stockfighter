import time
from api import buy, get_quote

venue = 'BMSTEX'
symbol = 'YMRI'
account = 'PFB66379220'

i = 0
while(i < 100):
	q = get_quote(venue, symbol)
	if(q.askSize > 0):
		print(q)
		o = buy(account, venue, symbol, q.ask, 1000)
		print (o)

	time.sleep(1)