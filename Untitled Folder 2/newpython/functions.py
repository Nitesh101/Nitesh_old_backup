#!/usr/bin/python
"""
def fun_name(arg):
	"this is prints"
	print "Hello"
	return
fun_name(2)

def  printme(str):
	print str
	return
printme("HELLO")
"""
def changelist(list1,list2):
	new1 = list1
	new2 = list2[:]
	new1.append(40)
	new2.append(300)
	print new1,new2
	return
list1 = [1,2,3,4]
list2 = [10,20,30,40]
changelist(list1,list2)
print list1,list2
