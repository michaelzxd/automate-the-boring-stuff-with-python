#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import re

def password_verify(password):
	ARegex = re.compile(r'[A-Z]+')
	result1 = ARegex.search(password)
	aRegex = re.compile(r'[a-z]+')
	result2 = aRegex.search(password)
	cRegex = re.compile(r'[0-9]+')
	result3 = cRegex.search(password)
	if result1 and result2 and result3:
		print('Password is strong!')
	else:
		print('Password is not strong enough!')


code = 'cde09'
password_verify(code)