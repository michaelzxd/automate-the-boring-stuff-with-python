#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
path = os.getcwd()
files = os.listdir(path)

finda = re.compile(r'[1-4]')
for file in files:
	if os.path.splitext(file)[1]=='.txt':
		for line in open(file):
			result = finda.findall(line)
			print(result)

