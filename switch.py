import time
import RPi.GPIO as io
import requests
import json

io.setmode(io.BCM)

door_pin = 23

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

params = {'accessKey': 'rMh3EEIsI0BgHBOd32iSOQsJMgKQIN62', 'streamName': 'toilet1', 'point': {'imgUrl': ' '} }

is_open = True

while True:
	print(io.input(door_pin))
	if io.input(door_pin):
		print("OPEN")
		is_open = True
		params['point'] = {'imgUrl': 'http://i.imgur.com/4rbuHMM.png'}
		requests.post("https://www.leftronic.com/customSend/", data=json.dumps(params))
		params['streamName'] = 'toilet2'
		requests.post("https://www.leftronic.com/customSend/", data=json.dumps(params))
	elif io.input(door_pin):
		print("CLOSED")
		is_open = False
		params['point'] = {'imgUrl': 'http://i.imgur.com/jsJQptq.png'}
		requests.post("https://www.leftronic.com/customSend/", data=json.dumps(params))
		params['streamName'] = 'toilet2'
		requests.post("https://www.leftronic.com/customSend/", data=json.dumps(params))
	time.sleep(0.5)

