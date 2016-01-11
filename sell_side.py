import time
from api import buy, sell, get_quote, get_order, cancel_order


venue = 'EFTEX'
symbol = 'UOZP'
account = 'IDS5292091 '

qty = 0
position = 0

while(True):
	q = get_quote(venue, symbol)
	bid = 1

	bought = False
	sold = False

	if(q.bidSize > 0):
		bid = q.bid + 1

	ask = 9999999
	if(q.askSize > 0):
		ask = q.ask - 1
	
	if(qty < 900):
		b = buy(account, venue, symbol, bid, 100)
		bought = True
	if(qty > -900):
		s = sell(account, venue, symbol, ask, 100)
		sold = True

	time.sleep(.5)

	if(bought):
		bo = cancel_order(venue, symbol, b.id)
		for f in bo.fills:
			qty = qty + f.qty
			position = position - (f.qty * f.price)

	if(sold):
		so = cancel_order(venue, symbol, s.id)
		for f in so.fills:
			qty = qty - f.qty
			position = position + (f.qty * f.price)	

	print('QTY: ' + str(qty))
	print('Position: ' + str(position))




