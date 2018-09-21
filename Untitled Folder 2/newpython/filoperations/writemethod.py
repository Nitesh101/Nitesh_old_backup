#!/usr/bin/python
fo = open("foo.txt","r+")
print "Name of the file:",fo.name
str = "This is 6th line"
fo.seek(0,2)
line = fo.write(str)
fo.seek(0,0)
for index in range(6):
	line = fo.next()
	print "Line no %d - %s"%(index,line)
fo.close()
