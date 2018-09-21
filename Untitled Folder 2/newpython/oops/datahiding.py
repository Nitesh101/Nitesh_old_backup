#!/usr/bin/python
class JustCount:
	__secretCount = 0
	def count(self):
		self.__secretCount += 1
		print self.__secretCount
counter = JustCount()
counter.count()
counter.count()
#print counter._JustCount__secretCount
