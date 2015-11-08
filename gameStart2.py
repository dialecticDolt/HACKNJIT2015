# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 21:14:44 2015

@author: William L. Ruys
"""
import asyncore
import socket
import sys
import os
import pickle 


endFlag = False;
isServer = False;
updateFlag = False;
turnFlag = True;
multiFlag = False;
currentTurn = 0;

HOST = 'localhost';
PORT = 50007;


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)

server = EchoServer(HOST, PORT)
asyncore.loop()
