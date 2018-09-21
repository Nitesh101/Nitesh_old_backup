#!/usr/bin/python

for num in range(10,21):
	remcntr =0
	for cntr in range(1,num+1,1):
		rem=num%cntr
		if(rem == 0):
			remcntr +=1
	if remcntr == 2:
		print num,"is a prime number"
	else:
		print num,"is not prime number"
