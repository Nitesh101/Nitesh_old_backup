#!/usr/bin/python
import os
import time
val = 0
print "Before fork"
os.fork()
os.fork()
os.fork()
os.fork()
os.fork()
print "After fork1"
val += 1
print "Val is",val
