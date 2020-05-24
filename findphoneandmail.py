#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#solve the problem of acsii code error
#import sys  
#reload(sys)  
#sys.setdefaultencoding('utf8') 

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext\.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ #username
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2.9})?
	)''', re.VERBOSE)

text = '''shippingoperation@chimbusco.com
yang.xinye@chimbusco.com
ma.yue1@chimbusco.com.cn
xia.shichao@chimbusco.com.cn
zhang.xiaodong2@chimbusco.com
song.jingyi@chimbusco.com
liu.jun3@chimbusco.com
gao.wei2@chimbusco.com
dong.chuanxi@chimbusco.com'''

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	print(groups[0])
	matches.append(groups[0])

if len(matches) > 0:
	
	print('Copied to clipboard')
	print('\n'.join(matches))
else:
	print('No phone numbers or email address found')

