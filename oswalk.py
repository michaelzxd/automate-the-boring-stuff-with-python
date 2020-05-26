#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
for folderName, subfolders, filenames in os.walk(os.getcwd()):
	print(folderName)
for subfolder in subfolders:
	print(subfolder)
for filename in filenames:
	print(filename)