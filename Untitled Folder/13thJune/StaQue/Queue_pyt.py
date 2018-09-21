#!/usr/bin/python3
from array import array

"""
sLen = input("Enter Queue length: ")

while not isinstance(sLen, int):
	print("Enter Integer value.")
	sLen = input("Enter stack length: ")
"""

class Queue():
	def __init__(self):
		self.sArray = array('i')

	def insert(self):
		if len(self.sArray)+1 > sLen:
			print("Queue is Full")
		else:
			value = input("Enter an Integer value: ")
			count = 1
			while count == 1:
				try:
					self.sArray.append(value)
					count = 2
				except TypeError:
					print("Enter integer values only.")
					value = input("Enter an Integer Value: ")

	def remove(self):
		self.sArray.pop(0)
	
	def display(self):
		if len(self.sArray) != 0:
			print(list(self.sArray))
		else:
			print('Empty List')

ex = Queue()

"""print("1: Insert\n2: Display\n3: Delete\n4: Exit")
opt = input("Enter your option: ")

while opt != 4:

	if opt == 1:
		ex.insert()

	elif opt == 2:
		ex.display()

	elif opt == 3:
		if 	len(ex.sArray) == 0:
			print("Stack is Empty, Insert Values.")
		else:
			ex.remove()

	print("1: Insert\n2: Display\n3: Delete\n4: Exit")
	opt = input("Enter your option: ")
"""
