#!/usr/bin/python
mylist = range(5)
itr = iter(mylist)
while True:
	try:
		index = itr.next()
		print index
	except StopIteration:
		break
