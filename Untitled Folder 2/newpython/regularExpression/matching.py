#!/usr/bin/python
import re
line = "Cats are smarter than dogs"
matchobj = re.match(r"dogs",line,re.M|re.I)
if matchobj:
	print matchobj.group()

else:
	print "no match"

matchobj = re.search(r"dogs",line,re.M|re.I)
if matchobj:
	print matchobj.group()
else:
	print "no match"
