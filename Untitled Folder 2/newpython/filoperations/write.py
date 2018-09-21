#!/usr/bin/python

outfile  = open('sample.txt','w')
outfile.write("My First output file")
outfile.close()


outfile = open('sample2.txt','w')
outfile.write("My second output file")
outfile.write("write some more")
outfile.close()


outfile = open('sample3.txt','w')
outfile.write('A revised ouput file!\n')
outfile.write('write some more.\n')
outfile.close()
outfile = open('sample3.txt','a')
outfile.write('A revised output file with append option!\n')
outfile.write('Write some more with append.\n')
outfile.close()

