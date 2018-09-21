#!/usr/bin/python
num = input("please enter a input: ")
cntr = 0
for val in num:
	if (val<1):
		print "negative number"
		continue
	cntr = cntr+val
print "the sum of val",cntr




