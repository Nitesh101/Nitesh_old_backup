import time,sys,mysql_py,os
from ctypes import *
import time
localtime = time.asctime(time.localtime(time.time()))
print "Scripts stat at :",localtime

os.chdir("/home/madisnit/Desktop/Executables_june_28_ble_server")
var = sys.argv
lis = var[1:]
print "\n"
print "Going to test",lis
fun = CDLL("./testapp.so")
def call_init(index):
	loop = int(lis[index+1])
	for number in range(loop):
		if lis[index] == "init":
			print "................initilize.........."
			fun.VITA_DM_Init()
		else:
			print ".................wrongEntary......."
			sys.argv(0)
