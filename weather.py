#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json, requests, sys

if len(sys.argv) < 1:
	print('Usage: weather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])
url = "http://api.openweathermap.org/data/2.5/forecast?q={'Beijing'}&appid={'5e3e232478a6bae9637fe7a35be76e30'}" 
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])