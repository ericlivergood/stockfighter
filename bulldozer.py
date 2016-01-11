from api import quote_stream, QuoteClientProtocol
from autobahn.twisted.websocket import WebSocketClientProtocol
from datetime import datetime

venue = 'RPOEX'
symbol = 'BSI'
account = 'RHP24199654'



quote_stream(account, venue, QuoteClientProtocol)
