"""
val = [1,2,3,4,5,6,7]	
print val.index(6)

my_list = [5.76,4.7,25.3,4.6,32.4,52.3,7.6,7.3,86]
print sorted(my_list)

def search(val,x):
	for index in range(len(val)):
		if val[index] == x:
			return index
	return -1
print search(val,5)
"""
val = [1,2,3,4,5,6,7,8]
val1 = int(input("please enter a value want: "))
for index in range(len(val)):
	if val[index] == val1:
		print "found index in list : ",index

