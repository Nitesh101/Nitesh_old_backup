#!/usr/bin/python
fo = open("foo.txt","w")
print "Name of the file: ",fo.name
print "Closed or not: ",fo.closed
print "Opening mode:",fo.mode
fo.close()
