#!/usr/bin/python
@staticmethod
def totfiles1():
	print "Number of text files(way1) is",textfile.ntfiles
	return


def totfiles():
	print "Number of text file(way2) is",textfile.ntfiles
	return
totfiles2 = staticmethod(totfiles)
textfile.totfiles1()
textfile.totfiles2()
