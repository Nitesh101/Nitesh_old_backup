#!/usr/bin/python
import os
import time
import sys
def print_time(processName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print "%s:%s"%(processName,time.ctime(time.time()))
processid = os.fork()
if processid:
	print_time("Parent Process:",1,)
	print processid
	parenpid = os.getpid()
	print "parent pid: ",parenpid
	parentppid = os.getpid()
	print "patent ppid: ",parentppid
	print processid
else:	
	print_time("child process:",7)
	print processid
	childpid = os.getpid()
	print "child pid",childpid
	childppid = os.getppid()
	print "child ppid",childppid
	
	sys.exit(0)
time.sleep(10)
