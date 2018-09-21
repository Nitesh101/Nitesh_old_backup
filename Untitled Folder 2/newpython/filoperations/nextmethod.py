#!/usr/bin/python
fo = open("foo.txt","r")
print "Name of the fil:",fo.name
for index in range(6):
	#line = fo.next()
	line = fo.readline();
	print "Line No %d- %s"%(index,line)
fo.close()
