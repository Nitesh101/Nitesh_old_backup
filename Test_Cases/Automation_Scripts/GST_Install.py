#!/usr/bin/python

from subprocess import PIPE,Popen
cmd='gst-inspect-1.0'
obj = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
data=obj.stderr.read()
if len(data) == 0: 
	print"Pass"
else:
	print"Fail"
