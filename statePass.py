# -*- coding: utf-8 -*-
"""
Test of Netorking Portion of HackNJIT
@author: William L. Ruys 
"""
import pickle
import socket
import sys
import threading
endFlag = False;
isServer = False;
updateFlag = True;
turnFlag = True;
HOST = 'localhost';
PORT = 50007;
stateBuffer = [];
msg = "";
currentTurn = 0;
eList = ["hey"]
eList.append("who");
wList = 123456;

class gameState:
    def __init__(self, eList, wList): 
        self.turnNumber = currentTurn;    """Attach Turn information"""
        self.eList = eList;               """State of all entities"""
        self.wList = wList;               """State of all world things"""

        
gState = gameState(eList, wList);
dataString = pickle.dumps(gState)
s = socket.socket();           
           
if isServer:
    try:
        s.bind(("", PORT))
    except (s.error , msg):
        print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    s.listen(1)
    client, addr = s.accept()
    while True:
        pickledState = client.recv(1024).decode()
        stateBuffer.append(pickle.loads(pickledState));
        if updateFlag:
            tempState = stateBuffer.pop();
            """tempState = tempState.update();"""
            dataString = pickle.dumps(tempState)
            client.send(dataString.encode())
        if endFlag:
            client.close()
            break;                   
else:
    s.connect((HOST, PORT));
    while True:
        if turnFlag:
            s.send(dataString.encode());
            print('hey')
            pickledState = s.recv(1024).decode();
            stateBuffer.append(pickle.loads(pickledState));
            print(stateBuffer.pop().eList)
            turnFlag = 0;
        if endFlag:
            break;  
            
            
