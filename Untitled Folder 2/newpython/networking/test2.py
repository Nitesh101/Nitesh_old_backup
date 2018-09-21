#import socket module
import socket               
 
# Create a socket object
s = socket.socket()         
host = '192.168.2.176' 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect((host, port))
 
# receive data from the server
print s.recv(1024)
# close the connection
s.close()       
