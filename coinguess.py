#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import random
guess = ''
while guess not in ('heads', 'tails'):
	print("Guess the coin toss! Enter heads or tails: ")
	guess = input()
	toss = random.randint(0,1)
	if toss == 1 and guess == 'heads':
		print('You got it!')
	elif toss == 0 and guess == 'tails':
		print('You got it!')
	else:
		print('Nope! Guess again!')
		guess = input()
		if toss == 1 and guess == 'heads':
			print('You got it!')
		elif toss == 0 and guess == 'tails':
			print('You got it!')
		else:
			print('Nope, you are already bad at this game.')


			