#!/usr/bin/python
tuple1 = "one","two"
tuple2 = 1,2
tuple3 = tuple1+tuple2
print tuple3


item1,item2,item3,item4 = tuple3
print item1,item2,item3,item4

mylist = ["a","b","c","d","end"]
print mylist

mylist[0],mylist[1],mylist[2],mylist[3] = tuple3
print mylist
