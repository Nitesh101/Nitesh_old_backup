#!/usr/bin/python
a = 40
print a
b = a
print b
c = [b]
print c
del a
b = 100
print b
c[0] = -1
