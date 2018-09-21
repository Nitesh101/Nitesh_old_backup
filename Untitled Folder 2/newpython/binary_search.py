#!/usr/bin/python
def binary_search(lst,seek):
	first = 0
	last = len(lst)-1
	found = None
	while first <= last:
		mid = (first + last)//2
		if lst[mid] == seek:
			found = mid
			break
		elif lst[mid] > seek:
			last = mid - 1
		else:
			first=mid+1
	return found
lst = [10,20,30,40,50,60,70]
print binary_search(lst,60)
