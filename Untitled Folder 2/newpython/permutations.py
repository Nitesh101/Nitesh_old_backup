#!/usr/bin/python
from itertools import permutations
from itertools import combinations
string = input("please enter a string: ")
itr = iter(string)
res = []
while True:
	try:
		res.append(itr.next())
	except StopIteration:
		break
count = 0
while count <= len(string):
	for num in combinations(res,count):
		print ''.join(num)
	count +=1
