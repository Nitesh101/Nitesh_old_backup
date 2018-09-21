#!/usr/bin/python


def bsort(lst):
	for item in range(len(lst)):	
		for item1 in range(len(lst)-1):
			if lst[item1]> lst[item1+1]:
				lst[item1],lst[item1+1]= lst[item1+1],lst[item1]
	return lst


def bsearch(lst,ele):
	low= 0
	high= len(lst)-1
	s_ele= "not found"
	
	while low<= high:
		mid= (low+high)/2
		if lst[mid]== ele:
			s_ele= mid
			break
		elif lst[mid]> ele:
			high= mid-1
		else:
			low= mid+1
	a= isinstance(s_ele,str)
	if a:
		return s_ele
	else:
		return lst[s_ele],s_ele

		
			


