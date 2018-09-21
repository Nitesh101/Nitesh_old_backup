#!/usr/bin/python
import thread
import time
def delay_loop(task,secs):
	print "Delay loop starts"
	print "%s:sleep %d seconds"%(task,secs)
	for counter in range(secs):
		time.sleep(counter)
	print "Delay loop ends"
def print_time(task,delay):
	count= 0
	while count < 5:
		time.sleep(delay)
		count += 1
		secs = time.time()
		print secs
		cal_time=time.ctime(secs)
		print cal_time
		print "%s:%s"%(task,cal_time)
	return
delay_loop("Task1",4)
print_time("Task2",2)

