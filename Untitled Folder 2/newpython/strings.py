#!/usr/bin/python
"""
str = 'Votarytech Learning Center'
print str.replace("Center","1")
print str.find("L")
print str.update('4','8')

print str[0:8],str[10::]
print str[1:20]
"""
list = ["this","is","python"]
print "To find index of list : "
print list.index("is")


list = ["this","is","python"]
print "To remove element from list : "
list.remove("is")
print list

list = ["this","is","python"]
print "To add elements in a list: "
list = list+["for"]
print list


list = ["this","is","python"]
print "To add element in end of list: "
list.pop()
print list


list = ["this","is","python"]
print "To add elment in specific index: "
list.insert(2,2009)
print list

list = ["this","is","python"]
print "delete a specific element in list: "
del list[1];
print list

list = ["this","is","python"]
print "To print element in multiple times : "
list = ["this"] * 4
print list


list = ["this","is","python"]
list.reverse()
print list



list = [5,6,6,7,8,1]
list.sort()
print list


list = [12,'nitesh','python',345]
list1 = [2009,'language']
list.extend(list1)
print "Extended list: ",list


dict   = {}
dict['one'] = "this is one"
dict[3] = "this is two"
dict = {'sep':'sales','code':876,'name':'nitesh','dep':'it'}
print dict



a = (1,2,3,"nitesh")
print list(a)
