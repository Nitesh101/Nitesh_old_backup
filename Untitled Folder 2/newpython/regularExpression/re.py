#!/usr/bin/python
import re

search = 'dog'
mystr = 'dog cat dog'
result = re.findall(search,mystr)
print result


pattern = re.compile(search)
result = pattern.findall(mystr)
print result

mystr  = "This is game of cat and dog"
result = pattern.findall(mystr)
print result
