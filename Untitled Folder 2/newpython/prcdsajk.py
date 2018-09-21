#!/usr/bin/python
def fun_sum(mylist):
	for index in range(len(mylist)):
		yield mylist[index]
val = input("please enter a value")
sum  = 0
for i in fun_sum(val):
	sum+=i 
print sum
