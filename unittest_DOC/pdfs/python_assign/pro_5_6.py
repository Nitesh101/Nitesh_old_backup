data=input("please enter a list: ")
seek=input("please enter a number which is need to search: ")
length=len(data)
for index in range(length):
	if(seek==data[index]):
		print "number is present\nindex of the number is", index
		break;
else:
	print seek,"is not present in the list"
