val=input("please enter the first number")
count=0
i=0
while(count!=val-1):
		if (count<=2):

		qout=count%val
		if(qout==0):
			print "not prim"
			break
		else:
			i+=1
		count+=1

print val,"is a number"

