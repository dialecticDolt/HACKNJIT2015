# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 16:19:47 2015

@author: William L. Ruys
"""
import socket
import sys
import pickle
s = socket.socket()

host = ''
port = 50007

class gameState:
    def __init__(self, eList, wList): 
        self.turnNumber = currentTurn;    """Attach Turn information"""
        self.eList = eList;
        self.wList = wList;    


try:
    s.bind((host, port))
except (s.error , msg):
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
    
print ('Socket bind complete')
s.listen(1)

while True:
   # the s.accept() command returns two variables that we save. client is
   # the client socket which we can use to send and receive data. the
   # address is the address bound to the client socket
   client, addr = s.accept()

   # print a success message for connection
   print ('Got connection from', addr)
   # create our message to send to server
   msg = 'Server: You are connected'
   print('hey')
   # we overwrite the msg variable with a message from the client. the
   # message is decoded and printed on the server
   msg = client.recv(1024).decode()
   msg2 = pickle.loads(msg)
   print(msg2.wList)
   
   # we then close the connection and exit our loop, terminating the
   # program
   client.close()
   break;
