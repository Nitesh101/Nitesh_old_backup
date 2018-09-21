val=input("please enter a number to check prime or not")

for count in range(2,val):
	qout=val%count
	if(qout==0):
		print "entered number is not a prime number"
		break;	

if(qout!=0):
	print val,"is a prime number"


