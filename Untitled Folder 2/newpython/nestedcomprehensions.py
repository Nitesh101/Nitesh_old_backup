#!/usr/bin/python
res = []
for val in range(2,4):
	for val2 in range(5,8):
		res.append(val)
print res

mylist = [val for val in range(2,4) for val2 in range(5,8)]
print mylist

res = []

for val in range(2,4):
	
	for val2 in range(5,8):
		res.append(val2)
print res

mylist2 = [val2 for val in range(2,4) for val2 in range(5,8)]
print mylist2
