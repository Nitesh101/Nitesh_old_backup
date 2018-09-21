#!/usr/bin/python
import re
string="python is scripting language"
matchobj=re.match(r'python',string)
print matchobj.group()
matchobj=re.search(r'is',string)
print matchobj.group()
matchobj=re.findall(r's',string)
print matchobj
s=string.split()
print s
s= re.split(' ',string)
print "split:",s
str1='123 asdf'
print re.sub(r'\D','',str1)
