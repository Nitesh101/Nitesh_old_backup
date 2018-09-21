val1=input("please enter the first number")
val2=input("please enter the last number")
i=0
if(val1>3):
	prime_list=[]
if(val1<=3):
	prime_list=[2,3]
	val1=4

for count in range(val1,val2):
	i=0
	for count1 in range(2,count-1):
#		print count1
		qout=count%count1
		if(qout==0):
			i=i+1
			break
#			continue
		else:
			pass
	if(i==0):
		prime_list.append(count)
		continue


print prime_list
