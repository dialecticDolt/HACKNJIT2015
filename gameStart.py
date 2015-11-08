# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 18:01:15 2015

@author: William L. Ruys
"""

"""
Starting Menu
Initialize Character
Create Map
loop:
    Initialize World Entities
    Wait for Keyboard Input
    Do Actions
    End turn
    if server wait
    if client send signal
    Update World
    send to client
    goto loop:
"""
import threading
import socket
import sys
import os
import pickle
import time

endFlag = False;
isServer = False;
updateFlag = False;
turnFlag = True;
multiFlag = False;
currentTurn = 0;

HOST = 'localhost';
PORT = 50007;

lockTurn = threading.Lock();
lockEnd = threading.Lock();
lockisServer = threading.Lock();
lockState = threading.Lock();

stateBuffer = []; """Store all the turns that have happened locally"""


class gameState:
    """This is what is communicated across the network"""
    def __init__(self, eList, wList):
        self.turnNumber = currentTurn;    """Attach Turn information"""
        self.eList = eList;               """State of all entities"""
        self.wList = wList;               """State of all world things"""

gState = gameState(["hey"], 1125);


class NJITHack(threading.Thread):
    def __init__(self):
        super(NJITHack, self).__init__()
    def run(self):
        global turnFlag
        global stateBuffer
        global isServer
        global endFlag
        global gState
        global lockTurn
        """
        STARTING MENU
        """

        """
        Initialize Character
        """

        """
        Create Map & Initialize World Entities
        """

        """Create GameState"""

        """
        Start Server Listening
        -Server starts waiting
        -Client will send signal if turnFlag is set
        -Server will send response on its turnFlag & recieve
        -
        """

        """
        All Actions and End Turn
        -All interactions
        -Invetory
        -Set End Turn Flag
        """

class Network(threading.Thread):
    def __init__(self):
        super(Network, self).__init__()

    def run(self):
        global turnFlag
        global stateBuffer
        global isServer
        global endFlag
        global gState
        global lockTurn
        global lockEnd
       # msg = "";
        s = socket.socket();
        dataString = pickle.dumps(gState);   #what ever state to send

        if isServer:
            #try:
            s.bind(("", PORT))
          #  except (s.error , msg):
           #     print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
          #      sys.exit()
            s.listen(1)
            client, addr = s.accept()
            print("Server is Listening");
            while True:
                pickledState = client.recv(1024).decode()
                stateBuffer.append(pickle.loads(pickledState));
                lockTurn.acquire();
                if turnFlag:
                    tempState = stateBuffer.pop();
                    """tempState = tempState.update();"""
                    dataString = pickle.dumps(tempState)
                    client.send(dataString.encode())
                lockTurn.release();
                lockEnd.acquire();
                if endFlag:
                    lockEnd.release();
                    client.close();
                    break;
                lockEnd.release();

        else:

            s.connect((HOST, PORT));
            while True:
                lockTurn.acquire();
                if turnFlag:
                    s.send(dataString.encode());
                    pickledState = s.recv(1024).decode();
                    stateBuffer.append(pickle.loads(pickledState));
                    turnFlag = False;
                lockTurn.release();
                lockEnd.acquire();
                if endFlag:
                    lockEnd.release();
                    break;
                lockEnd.release();

thread1 = NJITHack();
thread2 = Network();
thread1.start();
thread2.start();
