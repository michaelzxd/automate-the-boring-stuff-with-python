#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[2:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')

numOpen = min(3, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))