#!/usr/bin/python

num = input("please enter a value: ")
while(num<0):
	num=input("enter a value: ")
if num >1:
	for val in range(2,num):
		if(num%val)==0:
			print num,"is not prime number"
			break
	else:
		print num,"is number is prime"
else:
	print num,"is number is prime"
