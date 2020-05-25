#!/usr/bin/env python3
# -*- coding: UTF-8 -*-




a = input('Enter an adjective: ')
b = input('Enter a noun: ')
c = input('Enter a verb: ')
d = input('Enter a noun: ')


madlib = open('result_sentence.txt', 'w')
madlib.write('the %s panda walked to the %s and then %s,A nearby %s was unaffected by these events' % (a, b, c, d))
madlib.close()
madlib = open('result_sentence.txt', 'r')
lines = madlib.read()
print(lines)
madlib.close()