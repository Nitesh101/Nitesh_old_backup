import os,time,mysql_py,sys
from ctypes import *
import time

localtime = time.asctime(time.localtime(time.time()))
print "Script Start at :",localtime

os.chdir("/home/madisnit/Desktop/Executables_june_28_ble_server")
var = sys.argv
lis = var[1:]
print "\n"
print "Going to Test",lis

fun = CDLL("./testapp.so")

def call_init(index):
	loop = int(lis[index+1])
	for number in range(loop):
		if lis[index] == "init" :
			print "..............initilizeing..........."
			fun.VITA_DM_Init()
			fun.mysql_Connect()
		else:
			print ".................Wrong entry........"
			sys.exit(0)

			fun.mysql_Disconnect()
index=0
call_init(index)

