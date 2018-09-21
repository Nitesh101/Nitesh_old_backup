#!/usr/bin/python
import threading
import sys
class myThread(threading.Thread):
	global_val = 0
	def __init__(self,threadID,name,loopcount):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.loopcount= loopcount
		return
	def run(self):
		print "starting"+self.name
		threadlock.acquire()
		for counter in range(self.loopcount):
			myThread.global_val+=1
		threadlock.release()
		print "existing"+self.name
		return
#	def loop_count(self):
#		print "Global val is: ",global_val
	
#def addition(num):
#	count = mythread.global_val
#	for index in range(count):
#		num = num+num
#	print "the num after increament is: ",num
#	return

cmdlineargs = len(sys.argv)
if (cmdlineargs == 2):
	loops = int(sys.argv[1])

else:
	loops = 10000
print "total loops:",loops
threadlock = threading.Lock()
threads = []
thread1 = myThread(1,"thread1",loops)
thread2 = myThread(2,"thread2",loops)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print "Global value is:",myThread.global_val
