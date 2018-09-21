mylist=input("enter a list")
range_val=input("enter a range")
list1=[]
for index in range(len(mylist)):
	if (index==range_val):
		break
	list1.append(mylist[index])
		
print list1

