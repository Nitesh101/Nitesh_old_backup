#!/usr/bin/python
val = input("please enter a string: ")
val2 = input("please enter a string: ")
if(len(val) == len(val2)):
	s1 = sorted(val)
	s2 = sorted(val2)
	if(s1==s2):
		print "anagram"
	else:
		print "not anagram"
else:
	print "anangram"

