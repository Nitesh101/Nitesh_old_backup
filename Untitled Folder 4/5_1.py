#!/usr/bin/python
import os
def max_prod(length,*num):
	max1=-100;max2=-100
	for val in num:
		if(val>max1):
			max1 = val
	for val in num:
		if(val>max2)and(val<max1):
			max2 = val
	res=max1*max2
	return res

def bit_diff(num1,num2):
	bits=32;flips=0;bitshift=0
	while(bitshift<bits):
		status1=(num1>>bitshift)&1
		status2=(num2>>bitshift)&1
		if(status1!=status2):
			flips+=1
		bitshift+=1
	return flips

print "in parent"
childcnt=0
if(os.fork()==0):
#	list2=input("enter list:")
#	list2=[12,2,4,5,6]
#	length=len(list2)
#	res=max_prod(length,list2)
	res=max_prod(5,12,2,4,5,6)
	print "prod:",res
	exit(0)
elif(os.fork()==0):
	num1=input("enter num1:")
	num2=input("enter num2:")
	flips=bit_diff(num1,num2)
	print "flips:",flips
	exit(0)


while(childcnt<2):
	os.wait()
