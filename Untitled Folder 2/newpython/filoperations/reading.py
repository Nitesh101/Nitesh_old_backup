#!/usr/bin/python
infile = open("sample3.txt",'r')
contests = infile.read(10)
print (contests)

contests = infile.read()
print (contests)
infile.close()
