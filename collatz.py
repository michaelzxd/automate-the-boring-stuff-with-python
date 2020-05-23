#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def collatz(number):
	while int(number) != 1:
	    if int(number)%2 == 0:
		    number = int(number)/2
		    print(number)
		    
	    else:
		    number = 3 * int(number) +1
		    print(number)



while True:
	number = input('Please give an integer:  ')
	try:
		int(number)
	except ValueError:
	    print('Integer only, please')
	else:
		collatz(number)

# define the function first
# input is string, you need to convert string to number if you need calculation
# while True is a good method of looping until you get a right input



		    


