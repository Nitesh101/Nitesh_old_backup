#!/usr/bin/python
"""
list = ['abcd',3,456,'john']
list2 = [123,'nitesh']
print list
print list[0]
print list[:2]
print list[2:]
print list+list2
print list[-1]
print list*4

list1 = ["physics","chemistry",1997,2000];
list2 = [1,2,3,4,5,6,7];
print "list1[0]",list1[0]
print "list2[1:5]",list2[1:5]


list1 = ["physics","chemistry",1997,2000];
print list1
del list1[2]
print list1
"""

mylist = [10,20,30,40,50,60,70,80,90,100,110]
res = mylist[1:5:2]
print "1:",res

res = mylist[1::3]
print "2:",res

res = mylist[1::]
print "3:",res

res = mylist[-5:-1:2]
print "4:",res

listlen = len(mylist)
res = mylist[0:listlen:1]
print "5:",res


res = mylist[-listlen:-1:1]
print res



res = mylist[-listlen::1]
print res





