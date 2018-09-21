#!/usr/bin/python
#8
def selection_sort(lst):
	nitems = len(lst)
	for index1 in range(nitems-1):
		small = index1
		for index2 in range(index1+1,nitems):
			if lst[index2]<lst[small]:
				small = index2
		if index1!=small:
			lst[index1],lst[small] = lst[small],lst[index1]
	return lst
	#print lst 


lst = [50,30,10,20,40]
print selection_sort(lst)
