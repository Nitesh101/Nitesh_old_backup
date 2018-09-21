#!/usr/bin/python
import sys,thread
val = 0
def job1(thread_name,num=100):
	global_val = 2
	print "in %s",thread_name
	for index in range(num):
		val+=1
	print "in %s:"%(thread_name,val)
def job2(thread_name,num=100):
	global_val = 2
	print "in %s",thread_name
	print "in %s:%d"%(thread_name,val)
if(len(sys.argv)==2):
	try:
		thread.start_new_thread(job1,("thread1",int(sys.argv[1])))
		thread.start_new_thread(job2,("thread2",int(sys.argv[1])))
	except:
		print "error"
else:
	try:
		thread.start_new_thread(job1,("thread2",))
		thread.start_new_thread(job2,("thread2",))
	except:
		print "error"
while True:
	pass
