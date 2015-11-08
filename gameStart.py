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
import pygame
import pygcurse
import msvcrt
import time

endFlag = False;
isServer = True;
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
        exitFlag = True;
        reallyexitFlag = True;
        State = 1;
        while reallyexitFlag
            while exitFlag:
                """
                STARTING MENU
                """
                if State == 1:
                    print(" _   _      _ _____ _______   _    _          _____ _  __".center(100));
                    print("| \ | |    | |_   _|__   __| | |  | |   /\   / ____| |/ /".center(100));
                    print("|  \| |    | | | |    | |    | |__| |  /  \ | |    | ' / ".center(100));
                    print("| . ` |_   | | | |    | |    |  __  | / /\ \| |    |  <  ".center(100));
                    print("| |\  | |__| |_| |_   | |    | |  | |/ ____ \ |____| . \ ".center(100));
                    print("|_| \_|\____/|_____|  |_|    |_|  |_/_/    \_\_____|_|\_\ ".center(100));
                    print("==========================================================".center(100));
                    print("Created by Josef Mohrenweiser, Tyler Shuhnicki, and William Ruys".center(100));
                    print("****Single-Player".center(100));
                    print("----Multi-Player".center(100));
                if State == 2:
                    print(" _   _      _ _____ _______   _    _          _____ _  __".center(100));
                    print("| \ | |    | |_   _|__   __| | |  | |   /\   / ____| |/ /".center(100));
                    print("|  \| |    | | | |    | |    | |__| |  /  \ | |    | ' / ".center(100));
                    print("| . ` |_   | | | |    | |    |  __  | / /\ \| |    |  <  ".center(100));
                    print("| |\  | |__| |_| |_   | |    | |  | |/ ____ \ |____| . \ ".center(100));
                    print("|_| \_|\____/|_____|  |_|    |_|  |_/_/    \_\_____|_|\_\ ".center(100));
                    print("==========================================================".center(100));
                    print("Created by Josef Mohrenweiser, Tyler Shuhnicki, and William Ruys".center(100));
                    print("----Single-Player".center(100));
                    print("****Multi-Player".center(100));
                
                if State == 3:
                    name = input("Enter your Name".center(100));





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
            #lockEnd.acquire()
            endFlag = 1;
            #lockEnd.release();
        return;

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
                    lockState.acquire();
                    tempState = stateBuffer.pop();
                    """tempState = tempState.update();"""
                    dataString = pickle.dumps(tempState)
                    client.send(dataString.encode())
                    lockState.release();
                lockTurn.release();
                if endFlag:
                    client.close();
                    break;

        else:

            s.connect((HOST, PORT));
            while True:
                lockTurn.acquire();
                if turnFlag:
                    lockState.acquire()
                    s.send(dataString.encode());
                    pickledState = s.recv(1024).decode();
                    stateBuffer.append(pickle.loads(pickledState));
                    turnFlag = False;
                    lockState.release();
                lockTurn.release();
                if endFlag:
                    break;
                return;

thread1 = NJITHack();
thread2 = Network();
thread1.start();
thread2.start();
#print("Done")
sys.exit();
