#!/usr/bin/python

words = 'The quick brown fox jumps over the lazy dog'.split()
print words


stuff = [[word.upper(),word.lower(),len(word)] for word in words]
print stuff



words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [[word.upper(),word.lower(),len(word)] for word in words]
for word in stuff:
	print word
