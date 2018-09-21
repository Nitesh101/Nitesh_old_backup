#!/usr/bin/python
import math,sys
anumber = (int(input("please enter a number: ")))
try:
	print (math.sqrt(anumber))
except:
	print("Exception is",sys.exc_type)
	print("Bad value for square root")
	print("Using absolute value instead")
	print(math.sqrt(abs(anumber)))
print("End of program")
