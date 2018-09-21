#!/usr/bin/python

import random
count = random.randrange(10,20)
mylist = []
for index in range(count):
	num=random.randrange(-50,50)
	if num > 0:
		mylist.append(num)
print "list is:",mylist

