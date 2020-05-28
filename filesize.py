#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os,shutil



def filesize():
	file_dic = {}
	for file in os.listdir('.'):
		file_size = os.path.getsize(file)
		file_dic[file] = file_size
		
	value_list = file_dic.values()
	value_list.sort(reverse = True)
	new_file_dic = {v : k for k, v in file_dic.items()}
	for value in value_list:
		final_result = new_file_dic[value]+ 'size is: ' + str(value)
		print(final_result.rjust(40,'-'))
filesize()
