#!/usr/bin/python
import socket  
s = socket.socket()
host = "192.168.2.198"
port = 12345
s.connect((host,port))
print s.recv(1024)
s.send('welcome')
s.close()
