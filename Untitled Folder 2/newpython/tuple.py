#!/usr/bin/python
"""
tuple = ('abcd',1,2,3,44,'nitesh')
tuple2 = (546,'veera')
print tuple
print tuple[0:4]
print tuple*3
print tuple
print tuple+tuple2



mytuple = (10,20,30,40,50,60,70,80,90,100,110)
res = mytuple[1:5:2]
print "1:",res

res = mytuple[1::3]
print "2:",res

res = mytuple[1::]
print "3:",res

res = mytuple[-5:-1:2]
print "4:",res

tuplelen = len(mytuple)
res = mytuple[0:tuplelen:1]
print "5:",res


"""

mytuple  = (10,20,30)
mylist = list(mytuple)
mylist.append(40)
print mylist
mytuple=tuple(mylist)
print mytuple


mytuple = (10,20,(1,2,3),30)
mylist = list(mytuple)
mylist[1]=[1,2]
mylist[1][0]=10
mytuple = tuple(mylist)
print mytuple
