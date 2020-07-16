#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# step by step is ok, but pyautogui.typewrite(['down','down',]) does not work, do not know why,may be too fast

import pyautogui,time

nameField = (81,422)
submitButton = (34,665)
submitButtonColor = (119,119,119)
submitAnotherLink = (116,293)

formData = [{'name': 'Alice','fear':'eaversdroppers', 'source': 'wand','robocop':3,'comments': 'Tell bob I said hi.'},
            {'name': 'mimi','fear':'puppets', 'source': 'crystal ball','robocop':2,'comments': 'love u.'},
            {'name': 'Zhangxd','fear':'puppets', 'source': 'crystal ball','robocop':2,'comments': 'Please take the puppets.'}
             ]

pyautogui.PAUSE = 0.5

for person in formData:
	print('>>> 5 second pause to let user press ctrl-c <<<')
	time.sleep(5)
	print('Entering %s ' % (person['name']))
	pyautogui.click(nameField[0], nameField[1])

	pyautogui.typewrite(person['name'] + '\t')

	print('Entering %s ' % (person['fear']))
	pyautogui.typewrite(person['fear'] + '\t')

	print('Entering %s ' % (person['source']))

	if person['source'] == 'wand':
		# pyautogui.press(['down','down','\n','\t'])
		pyautogui.press('down')
		time.sleep(1)
		pyautogui.press('down')
		time.sleep(1)
		pyautogui.press('\n')
		time.sleep(1)
		pyautogui.press('\t')
	else:
		pyautogui.press('down')
		pyautogui.press('down')
		pyautogui.press('down')
		
		pyautogui.press('\n')
		
		pyautogui.press('\t')

	print('Entering %s ' % (person['robocop']))	
	if person['robocop'] == 3:
		pyautogui.typewrite(['right','right','right', '\t'])
	else:
		pyautogui.typewrite(['right', '\t'])

	print('Entering %s ' % (person['comments']))	
	pyautogui.typewrite(person['comments'] + '\t' + '\n')

	print('Click Submit.')
#	pyautogui.press('enter')
	
	time.sleep(5)
	pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])











