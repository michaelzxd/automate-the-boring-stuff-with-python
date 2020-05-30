#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')
