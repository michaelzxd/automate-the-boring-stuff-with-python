#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def add_to_inventory(inventory, addeditems):
	for item in set(addeditems):
		num = addeditems.count(item)
		if item in inventory.keys():
			
			inventory[item] = inventory[item] + num
			
		else:
			inventory[item] = num
	return inventory


inv = {'gold coin': 42,'rope':1}
print(inv)
dragonloot = ['gold coin', 'dagger', 'gold coin','gold coin','gold coin','ruby']
latestinv = add_to_inventory(inv, dragonloot)
print(latestinv)

