#!/usr/bin/python
count = 0
range2 = input("using start and stop values: ")
if len(range2)==2:
	start=range2[0]
	stop=range2[1]
	if start > stop:
		start = 10
		stop = 21
else:
	start = 10
	stop = 21
for num in range(start,stop+1,1):
	remcntr =0 
        for cntr in range(1,num+1):
                rem=num%cntr
                if(rem == 0):
                        remcntr +=1
       	if remcntr > 2:
               	print num,"is a prime number"
      	else:
               	print num,"is not prime number"

