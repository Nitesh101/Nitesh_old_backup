#!/usr/bin/python
import os
import time
print "Before fork"
os.fork()
print "After fork"
time.sleep(1)
os.fork()
print "After fork2"
os.fork()
print "After fork3"
