#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os,shutil

def select_copy():
	for file in os.listdir('.'):
		if file.endswith('.png'):
			source = os.path.abspath(file)
			shutil.copy(source,'/Users/xiaodongzhang/Documents/GitHub/automate-the-boring-stuff-with-python/pngfile')

select_copy()