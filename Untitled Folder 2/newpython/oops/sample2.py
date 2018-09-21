#!/usr/bin/python
class Point:
	def __init__(self,x=0,y=0):
		print "In Init"
		self.x = x
		self.y = y
	def __del__(self):
		class_name = self.__calss__.__name__
		print class_name,"destroyed"
pt1 = Point()
pt2 = pt1
pt3 = pt1
pt4 = Point(10,20)
pt5 = Point(10,20)
print id(pt1),id(pt2),id(pt3)
print id(pt4),id(pt5)
del pt1,pt2
print "Deleted pt1 and pt2 objects"
del pt3
del pt4,pt5
val1 = 10
print id(val1)
val2 = 10
print id(val2)
