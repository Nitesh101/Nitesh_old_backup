#!/usr/bin/python


for number in range(0,11,1):
	print number,
print "\n"
for number in range(0,11,3):
	print number,
print "\n"
for number in range(1,11,3):
	print number,
print "\n"
for number in range(11,1,-1):
	print number,
print "\n"
for number in range(11):
	print number,
print "\n"
for number in range(0,11):
	print number,
print "\n"



mylist = [1,3,5,7,9]
for cntr in mylist:
	print cntr
mytuple = (0,3,4,6,8,10)
for cntr in mytuple:
	print cntr
print 
low = 1
high = 5
for  value in range(low,high):
	print value
print



mylist = [10.22,122.33,18.3]
for cntr in mylist:
	print cntr

mylist = [10.22,122.33,18.3]
mylistlen = len(mylist)
for value in range(mylistlen):
	print value
