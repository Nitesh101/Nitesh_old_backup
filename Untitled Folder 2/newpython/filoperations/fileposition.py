#!/usr/bin/python
fo = open("fileseek.txt","w")
fo.write("Python is a great language.\nYeah its great!\n");
fo.close()

fo = open("fileseek.txt","r+")
str = fo.read(13);
print "Read string is:",str
position = fo.tell();
print "Current file position:",position
position = fo.seek(3,0);
str = fo.read(13);
print "Seek Beggining: read String is: ",str

position =fo.seek(2,1);
str = fo.read(6)
print "Seek Current: Again read,String is:",str


