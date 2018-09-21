#!/usr/bin/python
class textfile:
	ntfiles = 0
	@staticmethod 
	def totfiles1():
		print "Number of text files is:",textfile.ntfiles
		return
	def __init__(self,fname):
		textfile.ntfiles +=1
		self.name = fname
		self.fh = open(fname,"r")
		self.lines = self.fh.readlines()
		self.nlines = len(self.lines)
		self.nwords = 0
		self.wordcount()
	def wordcount(self):
		for line in self.lines:
			words=line.split()
			self.nwords += len(words)
	def grep(self,target):
		for line in self.lines:
			if line.find(target) >= 0:
				print line
	def totfiles2():
		print "Number of files is:",textfile.ntfiles
		return
	totfiles=staticmethod(totfiles2)

file1 = textfile('file1.txt')
file2 = textfile('file2.txt')
print 'The number of text files open is:',textfile.ntfiles
print "some info about them(name,lines,words):" 
for myfile in [file1,file2]:
	print myfile.name,myfile.nlines,myfile.nwords
file1.grep('example') 


textfile.totfiles1()
textfile.totfiles()
