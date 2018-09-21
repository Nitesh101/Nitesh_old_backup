#!/usr/bin/python
import os,re

class camera:
	
	def camera_log(self):
		os.system("adb logcat| grep camera>cam.txt")
	def read_camera_cnt(self):
		fp=open("cam.txt","r")
		buff=fp.readline()
		data = list(buff)
		for val in data:
			if re.search(r'Opening camera 0 with camera1 API',val):
		#		print val
		#	print count
	'''	for val  in buff:
			if re.search(r'D/aaa_state_camera_preview',val):
                                print val

	#	print "cam_open:",len(cam_open)
	#	print "cam_close:",len(cam_close)
'''
cam=camera()
cam.camera_log()
cam.read_camera_cnt()
print count
