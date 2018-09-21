#!/usr/bin/python
import p_sortsearch

lst= [3,2,1,8,9,23,62,12]
print "original list ",lst
lst= p_sortsearch.bsort(lst)
print "after sorting ",lst
res= p_sortsearch.bsearch(lst,12)
print "(element,index)= ",res
