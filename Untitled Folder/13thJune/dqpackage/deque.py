#!/usr/bin/python

lst= []

def insert_rear(ele):
	lst.insert(0,ele)

def insert_front(ele):
	lst.append(ele)

def delete_front():
	if len(lst)!=0:	
		lst.pop(0)
	else:
		print "underflow"

def delete_rear():
	if len(lst)!= 0:
		lst.pop()
	else:
		print "underflow"

def display():
	print lst

"""
while 1:
	ch= input("Enter option for 1.insert_rear , 2.insert_front , 3.delete_front , 4.delete_rear , 5.display: ")
	if ch== 1:
		ele= input("Enter a element: ")
		insert_rear(ele)
	elif ch== 2:
		ele=input("Enter a element: ")
		insert_front(ele)
	elif ch== 3:
		delete_front()
	elif ch== 4:
		delete_rear()
	elif ch== 5:
		display()
	else:
		exit()
"""
