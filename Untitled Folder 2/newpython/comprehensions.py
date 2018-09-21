#!/usr/bin/python

mylist = range(10)
for val in mylist:
	val = val**2
	print val,
print ('/n')

mylist = range(10)
myset = [val ** 2 for val in mylist]
print myset


mylist = range(13)
for val in mylist:
	val = 2**val
	print val,
myvector = [2**val for val in mylist]
print myvector 


