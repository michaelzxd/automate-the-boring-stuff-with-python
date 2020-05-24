#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

def my_strip(a_str,c=None):
	if c == None:
		ARegex = re.compile(r'\w+')
		result1 = ARegex.search(a_str)
		print(result1.group())
	else:
		print(a_str.replace(c,''))
		
	


b = '    adfw    '

my_strip(b,c = 'f')
my_strip(b)