#!/usr/bin/python
import os,re
class camera:
	def camera_log(self):
		os.system("adb logcat| grep camera>camera.txt")
#os.system("adb logcat grep camera>camera.txt")
#cam_open=0;cam_close=0;
	def read_camera_cnt(self):
		fp=open("camera.txt","r")
		buff=fp.read()
#cam_open=buff.count("Camera open",0,len(buff))
#cam_close=buff.count("Camera close",0,len(buff))	
#		cam_open=re.findall(r'Camera open',buff,re.M|re.I)
#		cam_close=re.findall(r'camera close',buff,re.M|re.I)
		cam_open=re.findall(r'opening camera',buff,re.M|re.I)
		cam_close=re.findall(r'destroying camera',buff,re.M|re.I)
#cam_open-=1;
#cam_close-=2;

		print "cam_open:",len(cam_open)
		print "cam_close:",len(cam_close)

cam=camera()
cam.camera_log()
cam.read_camera_cnt()

