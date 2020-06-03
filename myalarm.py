#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time, subprocess

timeleft = 10
while timeleft > 0:
	print('timeleft: ' + str(timeleft)  + '\n')
	time.sleep(1)
	timeleft = timeleft - 1

print('time is over!')
subprocess.Popen(['open', 'alarm.wav'])