import json
import requests
import websocket
import random 
import time
ws=websocket.WebSocket()
while(True):
	try:
		ws.connect('ws://127.0.0.1:8000/show/subeshpoudel')
		break
		
	except:
	 print("connecting..........")
for i in range(1000):
	time.sleep(2)
	ws.send(json.dumps({'value':random.randint(100,500),'node':random.randint(0,4)}))

