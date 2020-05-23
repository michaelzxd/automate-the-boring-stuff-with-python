#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

tableData = [['apple', 'orange', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
colWidths = [0] * len(tableData)



def find_long(alist):
	num = 0
	for item in alist:
		if len(item) > num:
			num = len(item)
		else:
			pass
	return num



def printTable(alist):
	colWidths = [0] * len(tableData)
	colWidths[0] = find_long(tableData[0])
	colWidths[1] = find_long(tableData[1])
	colWidths[2] = find_long(tableData[2])
	colWidths.sort()
	width = colWidths[-1]
	for m in tableData:
		for n in m:
			print(n.rjust(width, ' '))

printTable(tableData)

		
