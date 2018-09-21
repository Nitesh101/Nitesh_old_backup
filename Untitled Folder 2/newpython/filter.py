#!/usr/bin/python

def evennums(element):
	rem = (element % 2 )
	if rem == 0:
		return True
	return False

numbers = range(1,20)
mylist = filter(evennums,numbers)
print mylist


numbers = range(10)
mylist = filter(lambda val:val%2==0,numbers)
print mylist
mylist = filter(lambda val:val%2!=0,numbers)
print mylist
