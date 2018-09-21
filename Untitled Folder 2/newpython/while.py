#!/usr/bin/python
number = [6,5,5,4,3,8]
val = 0
count = 0
while(count<len(number)):
	val = val+number[count]
	count +=1
print val

number = input("please enter a number: ")
val = 0 
count = 0
while(number>0):
	val = val+number
	number = input("please enter a number: ")

else:	
	print val
