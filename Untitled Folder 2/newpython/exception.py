#!/usr/bin/python

import math
number = int(input("please enter an integer: "))

if number<0:
	raise RuntimeError("you can't use a negative number")


print(math.sqrt(number))
print ("End of Program")
