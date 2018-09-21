mylist=input("enter a list")
val=input("enter values to skip")
list1=[]
for index in range(len(mylist)):
	if (mylist[index]==val):
		continue
	list1.append(mylist[index])
		
print list1

