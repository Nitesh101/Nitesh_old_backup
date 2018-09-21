#!/usr/bin/python
def locate(lst,seek):
	found = None
	for cntr in range(len(lst)):
		if lst[cntr] == seek:	
			found = cntr
			break
		
	return found
lst = [2,74,8,28,29,20,2,3]
print locate(lst,28)


def display(lst,value):
	"display location if found"
	position = locate(lst,value)
	if position  != None:
		print "value","in list found at location",position
	else:
		print "value",value,"not in list"
	return
display(lst,28)
