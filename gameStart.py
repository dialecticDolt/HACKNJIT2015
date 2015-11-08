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
import msvcrt
import time
from world import *

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
statusBuffer = ""; """Description of Past Action"""

class gameState:
    """This is what is communicated across the network"""
    def __init__(self, eList, wList):
        self.turnNumber = currentTurn;    """Attach Turn information"""
        self.eList = eList;               """State of all entities"""
        self.wList = wList;               """State of all world things"""

def merge(gameState1, gameState2):
    gameState2.eList[0] = gameState1.eList[0]



#def kbfunc():
#    x=msvcrt.kbhit()
#    if x:
#        ret = msvcrt.getch()
#    else:
#        ret = False;
#    return ret

def invScreen():
    """DONT NEED THIS"""
def statScreen():
    """WAITING ON TYLER CODE"""
    print()

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
        global multiFlag
        exitFlag = True;
        reallyexitFlag = True;
        State = 1; p= True;
        os.system("cls")
        while reallyexitFlag:
            while exitFlag:
                """
                STARTING MENU
                """
                if State == 1 and p:
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
                    p = False;
                if State == 2 and p:
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
                    p = False;
                x = kbfunc()
                if x!= False and x.decode() == 's':
                    State = 2;
                    os.system("cls");p = True;
                if x!= False and x.decode() == 'w' and State != 1:
                    State =1;
                    os.system("cls");p = True;
                if x!= False and x.decode() == '\r':
                    if State ==1:
                        State =3;
                    else:
                        State=4;
                        multiFlag = True;
                    exitFlag = False;
                    os.system("cls");
                else:
                    time.sleep(0.01);
            exitFlag = True; p = True;
            while exitFlag:
                if State == 4 and p:
                    print(" _   _      _ _____ _______   _    _          _____ _  __".center(100));
                    print("| \ | |    | |_   _|__   __| | |  | |   /\   / ____| |/ /".center(100));
                    print("|  \| |    | | | |    | |    | |__| |  /  \ | |    | ' / ".center(100));
                    print("| . ` |_   | | | |    | |    |  __  | / /\ \| |    |  <  ".center(100));
                    print("| |\  | |__| |_| |_   | |    | |  | |/ ____ \ |____| . \ ".center(100));
                    print("|_| \_|\____/|_____|  |_|    |_|  |_/_/    \_\_____|_|\_\ ".center(100));
                    print("==========================================================".center(100));
                    print("Created by Josef Mohrenweiser, Tyler Shuhnicki, and William Ruys".center(100));
                    print("****Server".center(100));
                    print("----Client".center(100));
                    p = False;
                if State == 5 and p:
                    print(" _   _      _ _____ _______   _    _          _____ _  __".center(100));
                    print("| \ | |    | |_   _|__   __| | |  | |   /\   / ____| |/ /".center(100));
                    print("|  \| |    | | | |    | |    | |__| |  /  \ | |    | ' / ".center(100));
                    print("| . ` |_   | | | |    | |    |  __  | / /\ \| |    |  <  ".center(100));
                    print("| |\  | |__| |_| |_   | |    | |  | |/ ____ \ |____| . \ ".center(100));
                    print("|_| \_|\____/|_____|  |_|    |_|  |_/_/    \_\_____|_|\_\ ".center(100));
                    print("==========================================================".center(100));
                    print("Created by Josef Mohrenweiser, Tyler Shuhnicki, and William Ruys".center(100));
                    print("----Server".center(100));
                    print("****Client".center(100));
                    p = False;
                x = kbfunc()
                if x!= False and x.decode() == 's':
                    State = 5;
                    os.system("cls");p = True;
                if x!= False and x.decode() == 'w' and State != 4:
                    State =4;
                    os.system("cls");p = True;
                if x!= False and x.decode() == '\r':
                    if State ==4:
                        isServer = True;
                    else:
                        isServer = False;
                        State = 6;
                    exitFlag = False; State = 3; break;
                else:
                    time.sleep(0.01);
            if State == 6:
                HOST = str(raw_input("Enter the host address:"));
                State = 3;
            #if State == 3:
            #    name = str(raw_input("Enter your name: "));




            """
            Initialize Character
            """

            """
            Create Map & Initialize World Entities
            """
            wList = "";
            eList = [];
            if multiFlag:
                eList.append(Character("Player2", True));
            eList.append(Character("Player1", True));
            #Populate eList
            """Create GameState"""

            while True:
                z = kbfunc()
                if z != False:
                    if z.decode() == 'w':
                        eList[isServer].moveUp()
                    if z.decode() == 's':
                        eList[isServer].moveDown()
                    if z.decode() == 'a':
                        eList[isServer].moveLeft()
                    if z.decode() == 'd':
                        eList[isServer].moveRight()
                    else:
                        time.sleep(0.01)
                    """Create GameState"""
                    eList[isServer].update()
                    lockState.acquire();
                    gState = gameState(eList, wList);
                    lockState.release();
                    turnFlag = True;

                    if multiFlag:
                        while turnFlag:
                            time.sleep(0.01)

                    for e in eList:
                        e.update()
                    """
                    LOOP: START GAME
                    All Actions and End Turn
                    -All interactions
                    -Invetory
                    -Set End Turn Flag on both deaths.
                    """
            endFlag = True; #If this is true the game ends;

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
        s = socket.socket();
        dataString = pickle.dumps(gState);   #what ever state to send

        if isServer:
            s.bind(("", PORT))
            s.listen(1)
            client, addr = s.accept()
            print("Server is Listening");
            while True:
                lockState.acquire();
                pickledState = client.recv(1024).decode()
                stateBuffer.append(pickle.loads(pickledState));
                lockTurn.acquire();
                if turnFlag:
                    tempState = stateBuffer.pop();
                    tempState = merge(tempState, gState);
                    dataString = pickle.dumps(tempState)
                    client.send(dataString.encode())
                    turnflag = False;
                lockTurn.release();
                lockState.release();
                if endFlag:
                    client.close();
                    break;
        else:
            s.connect((HOST, PORT));
            while True:
                lockTurn.acquire();
                if turnFlag:
                    lockState.acquire()
                    dataString = pickle.dumps(gState);
                    s.send(dataString.encode());
                    pickledState = s.recv(1024).decode();
                    stateBuffer.append(pickle.loads(pickledState));
                    gState = stateBuffer.pop()
                    turnFlag = False;
                    lockState.release();
                lockTurn.release();
                if endFlag:
                    break;

thread1 = NJITHack();
if multiFlag:
    thread2 = Network();
thread1.start();
if multiFlag:
    thread2.start();
#print("Done")
sys.exit();
