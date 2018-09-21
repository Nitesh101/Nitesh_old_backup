#!/usr/bin/python
"""
#if
myinput = input("enter a input: ")
dtype = type(myinput)
if(dtype== int):
	print "your input",myinput,"data type is",dtype


myinput = input("enter a input: ")
res = isinstance(myinput,int)
if(res == True):
	print "your input ",res,"data type is",dtype


#ifelse
myinput = input("enter a input: ")
dtype = type(myinput)
if(dtype == int):
	print "your input ",myinput,"data type is",dtype
else:
	
	print "your input not integer ",myinput

#ifelse
number = 23
guess = input("Enter a integer: ")
if guess == number:
	print "congratulations you got number"
elif guess < number:
	print "No,it is  littile higher than that"
else:
	print "No,it is little lower than that"
print "Done"

#else if ladder
myinput = input("Enter input: ")
dtype = type(myinput)
if (dtype == int):
	print "your input",myinput,"your dtype",dtype

elif(dtype == float):
	print "your input",myinput,"your dtype",dtype

elif(dtype == str):
	print "your input",myinput,"your dtype",dtype
elif(dtype == list):
	print "your input",myinput,"your dtype",dtype
elif(dtype == tuple):
	print "your input",myinput,"your dtype",dtype
elif(dtype == dict):
	print "your input",myinput,"your dtype",dtype
else:
	print "Unknow input"

"""
#nestedif

