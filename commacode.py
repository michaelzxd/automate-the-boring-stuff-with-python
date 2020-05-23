#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

spam = ['apples', 'bananas', 'tofu', 'cats']
def list_str(alist):
	alist[-1] = 'and ' + alist[-1]
	astring = ''
	for item in alist:
		astring = astring + item + ', '

	print(astring[:-2])


 
list_str(spam)