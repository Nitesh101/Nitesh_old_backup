from StaQue.Queue_pyt import Queue
from StaQue.stack_pyt import Stack

opt = input("1. Stack\n2. Queue")
if opt == 1:
	ex = Stack()

	print("1: Insert\n2: Display\n3: Delete\n4: Exit")
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

elif opt ==2:
	ex = Queue()

	print("1: Insert\n2: Display\n3: Delete\n4: Exit")
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
else:
	print("Enter correct option.\n1.Stack\n2.Queue")

	
