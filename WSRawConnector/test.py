from wss import WebSocketConnectorThread
from time import sleep
import logging
import sys
import json

log = logging.getLogger('wss')
log.setLevel(logging.DEBUG)
log_sh = logging.StreamHandler(sys.stdout)
log_sh.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s : %(message)s'))
log.addHandler(log_sh)

wss = WebSocketConnectorThread(url="wss://api.hitbtc.com/api/2/ws")
wss.start()
wss.connected.wait()
wss.send({'method': 'getSymbols', 'params': None, 'id': wss.gen_str_id()})
wss.send({'method': 'subscribeTicker', 'params': {'symbol': 'BTCUSD'}, 'id': wss.gen_str_id()})

while True:
  sleep(1)
  try:
    print(wss.recv())
  except:
    pass