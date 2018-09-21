#!/usr/bin/python
str = "this is string example ...wow"
print "capitalize:",str.capitalize()
print "centered string:",str.center(40,'a')

print "upper case:",str.upper() 



str1 = "this is string example...wow"
str2 = "exam"
print str1.find(str2)
print str1.find(str2,40)
print str1.index(str2)
#print "Hello %*s"%(5),%(str1)

str = "this string example ...wow";
str = str.encode('base64','strict');
print "Encode String: " + str;
print "Decode String: "+ str.decode('base64','strict')
