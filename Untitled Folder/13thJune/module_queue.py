from Queue_pyt import Queue

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
