#!/usr/bin/python
import sys
from Dashboard import create_dashboard
lis=sys.argv
lis=lis[1:]
path=lis[0]
mylist=lis[1:]

fp = open(path, "r")
result = fp.read().rstrip()                    #rstrip for removing the \n                      
if result == "Pass":
	mylist.append(result)
	create_dashboard(mylist)
	print mylist[0]," Executed succesfully"
else:
	mylist.append(result)
	create_dashboard(mylist)
	print mylist[0]," Failed Error found "

