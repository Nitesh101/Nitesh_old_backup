#!/usr/bin/python
def fib(totalnums):
	v1,v2 = 0,1
	while v2 < totalnums:
		print v2
		v1,v2=v2,v1+v2
	return
def fib2(totalnums):
	res = []
	v1,v2=0,1
	while v2 < totalnums:
		res.append(v2)
		v1,v2 = v2,v1+v2
	return res
