#!/usr/bin/python
import sys,getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try: 
		opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'getopts_test.py -i <inputfile> -o <ouputfile>'
		sys.exit(2)
	for opt,arg in opts:
		if opt == '-h':
			print 'usage: getopts_test.py -i<inputfile> -o<outputfile>'
			sys.exit()
		elif opt in ("-i","__ifile"):
			inputfile= arg
		elif opt in ("-o","__ofile"):
			outputfile = arg
	print 'input file  is ',inputfile
	print 'output file is',outputfile
	return
if __name__ == '__main__':
	main(sys.argv[1:])
 
