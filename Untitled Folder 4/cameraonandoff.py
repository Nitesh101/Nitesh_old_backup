
import re
count = 0
count1 = 0
fo =  open("camera1.txt","r")
system = fo.readlines()
data = list(system)
#print data
#data = "D/aaa_state_camera_preview"
for val in data:
	if re.search(r"Opening camera 0 with camera1 API",val):
		print val
		count += 1
for val in data:
        if re.search(r"D/aaa_state_camera_preview",val):
                print val
                count1 += 1
        

	
print "opening camera",count
print "closing camera",count1



'''
#
class textfile:
        ntfiles=0
	global count
        def __init__(self,fname):
                textfile.ntfiles+=1
                self.name=fname
                self.fh=open(fname,"r")
                self.lines=self.fh.readlines()
                self.nlines=len(self.lines)
                print self.nlines
            #    self.nwords=0
           #     self.wordcount()
        def grep(self,target):
                for line in self.lines:
                        if line.find(target)>=0:
                                print line
				print len(self.line)
obj=textfile("camera1.txt")
##file.txt have this program as data
#obj2=textfile("camera.txt")

obj.grep("Opening camera 0 with camera1 API")
'''	
