#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
for filename in os.listdir(os.getcwd()):
	if filename.endswith('.txt'):
		print(filename)