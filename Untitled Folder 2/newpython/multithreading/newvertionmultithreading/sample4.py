#!/usr/bin/python
import threading
import sys
class global_values(threading.Thread):
	global_val = 0
	def __init__(self,threadID,name,loopcount):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.loopcount = loopcount
		return
	def run(self):
		print "starting" + self.name
		
