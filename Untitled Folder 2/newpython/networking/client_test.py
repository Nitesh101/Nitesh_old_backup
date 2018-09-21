import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Connect the socket to the port on the server given by the caller
server_address = ('192.168.2.198', 22)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
 
try:
 
     message = 'This is the message.  It will be repeated.'
     print >>sys.stderr, 'sending' 
     for x in range (0,1):
       name=raw_input ('what is ur name: ')
       print type(name)
       sock.send(name)
       print sock.recv(1024)
 
finally:
     sock.close()
