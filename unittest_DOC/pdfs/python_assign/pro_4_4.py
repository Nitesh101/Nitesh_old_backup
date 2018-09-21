val1=input("enter a number")
val2=input("enter a number")
val3=input("enter a number")
if (val1>val2):
	if (val3>val1):
		print "greatest is", val3
		print "smallest is", val2
	if (val3<val1):
		print "greatest is", val1
		print "smallest is", val2
	if (val3==val1):
		print "greatest is", val1
		print "smallest is", val2

if (val2>val1):
	if (val3>val2):
		print "greatest is", val3
		print "smallest is", val1
	if (val3<val2):
		print "greatest is", val2
		print "smallest is", val1
	if (val3==val2):
		print "greatest is", val2
		print "smallest is", val1


elif (val2==val1):
	print "both are same"
	if (val3>val1):
		print "greatest is", val3
		print "smallest is", val2
	if (val3<val1):
		print "greatest is", val1
		print "smallest is", val3

