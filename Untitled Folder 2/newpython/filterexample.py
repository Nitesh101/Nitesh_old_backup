#!/usr/bin/python
"""
numlist = [3,4,5,6]
reslist = []
for num in numlist:
	if num > 4:
		reslist.append(num)
print reslist

num = [3,5,6,7]
reslist = [val for val in numlist if val>4]
print reslist

reslist = filter(lambda val:val > 4,numlist)
print reslist

mylist = [3,4,5]
numele = len(mylist)
for index in range(numele):
	mylist[index]+=3
print mylist

mylist = [num+3 for num in mylist]
print mylist

mylsit = map(lambda val:val+3,mylist)
print mylsit
"""
mylist = [3,4,5]
for index,item in enumerate(mylist):
	print index,item


mylist = ['tic','tac','toe']
for index,val in enumerate(mylist):
	res =  "".join(val)
	print (res, end=" "),





