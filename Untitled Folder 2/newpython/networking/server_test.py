from socket import *
HOST = '192.168.2.199'
PORT = 22
serversocket = socket(AF_INET,SOCK_STREAM)
serversocket.bind((HOST,PORT))
print 'bind success'
serversocket.listen(5)
print 'listening'
while True:
     (clientsocket, address) = serversocket.accept()
     print ("Got client request from",address)
     #clientsocket.send('True')
     data = clientsocket.recv(1024)
     print data
     clientsocket.send('True')
     clientsocket.close()
