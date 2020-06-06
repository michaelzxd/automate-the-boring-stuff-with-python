#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyautogui, time
time.sleep(5)
pyautogui.click()


distance = 100
while distance > 0:
	pyautogui.dragRel(distance, 300, duration=0.2)
	distance = distance - 5
	pyautogui.dragRel(300,distance, duration=0.2)
	pyautogui.dragRel(-distance, 300, duration=0.2)
	distance = distance - 5
	pyautogui.dragRel(300,-distance, duration=0.2)