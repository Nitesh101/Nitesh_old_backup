#!/usr/bin/python
import sys
#import re

fo = open("log1.txt", "r")
if len(sys.argv) >= 2:
	if str(sys.argv[1]) == "kn":
		st = "KnockOnPowerController"
	elif str(sys.argv[1]) == "wi":
		st = "WifiController"
	elif str(sys.argv[1]) == "ba":
		st = "BatteryObserver"
	elif str(sys.argv[1]) == "po":
		st = "PowerManagerService"
	else:
		print "Unknown"
		sys.exit()
else:
	st = "Touch"
for line in fo:
	if st in line:
		print line,
