#!/usr/bin/python
def squrofpositive(num):
	total = 0
	list1 = []
	for val in num:
		if  val > 2:
			total = val*val
			list1.append(total)
	print "total positive squr is:",list1
	return
print squrofpositive([1,2,3,4])
