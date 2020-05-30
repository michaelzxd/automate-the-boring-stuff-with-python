#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://mail.qq.com/')

emailElem = browser.find_element_by_id("u")
emailElem.send_keys('403533049')
passwordElem = browser.find_element_by_id("p")
passwordElem.send_keys('')
passwordElem.submit