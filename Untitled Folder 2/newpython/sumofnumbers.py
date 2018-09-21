#!/usr/bin/python
"""
num = [1,2,3,4,5,6,7]
res = 0
for val in num:
	res=res+val
print"sum of all numbers",res
"""

numlist = int(input("Enter number in list(+ve or -ve): "))
count = 0
sumnums = 0
while (count < numlist):
	sumnums	= numlist[count]
	if(numlist<0):
		count +=1
		continue
	count +=1
	sumnums += numlist
print "sum of numbers",sumnums	
