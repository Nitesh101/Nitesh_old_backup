#!/usr/bin/python
mydata = input("Enter input(List,Tuple ,dictionary or set):")
if(isinstance(mydata,list)==True):
	print "Enter list",mydata
elif(isinstance(mydata,tuple)==True):
	print "Enter Tuple",mydata

elif(isinstance(mydata,dict)==True):
	print "Enter dictionary",mydata
elif(isinstance(mydata,set)==True):
	print "Enter set",mydata
else:
	print "Expected only list,Tuple,Dictinary  or set"
