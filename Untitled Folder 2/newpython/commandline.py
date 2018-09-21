#!/usr/bin/python
import sys
print "command line argument are: "
total_sum = 0
total_nums = len(sys.argv)
if total_nums > 1:
	for index in range(1,total_nums):
		num = int(sys.argv[index])
		total_sum += num
	print(total_sum)
else:
	print ("No argument passed")

