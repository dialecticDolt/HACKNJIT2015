import random
import sys

class world:
    def __init__(floors):
        self.floors = floors

class floor:
    def __init__(self, sizex, sizey, roomnum):
        self.rooms = []
        self.space = [[' ' for x in range(sizex)] for x in range(sizey)]
        self.x = sizex
        self.y = sizey
        self.roomnum = roomnum
    def create(self):
        for i in range (0, self.roomnum):
            temp = room()
            temp.create(self.x, self.y)
            self.rooms.append(temp)
        for i in range(0, self.y):
            for j in range(0, self.x):
                if (self.inRoom(j,i)[1] == True):
                    (self.space)[j][i] = '.'
                elif self.isWall(j, i):
                    (self.space)[j][i] = '='
                else:
                    (self.space)[j][i] = ' '
    def inRoom(self, xpos, ypos):
        for i in range(0, self.roomnum):
            if (self.rooms[i]).inRoom(xpos,ypos):
                return (i,True)
        return (-1,False)
    def isWall(self, xpos, ypos):
        for i in range(0, self.roomnum):
            if (self.rooms[i]).isWall(xpos,ypos):
                return True
        return False
    def drawFloor(self):
        print '+'*((self.x)+2)
        for i in range(0, self.y):
            line = '+'
            for j in range (0, self.x):
                line += self.space[j][i]
            line += '+'
            print(line)
        print '+'*((self.x)+2)
            

class room:
    def __init__(self):
        self.sizex = random.randrange(1,8,2)
        self.sizey = random.randrange(1,8,2)
    def create(self, x, y):
        self.centerx = 0
        self.centery = 0
        while (self.centerx-(self.sizex-1)/2 < 0 or self.centerx + (self.sizex-1)/2 >= x):
            self.centerx = random.randrange(0,x)
        while (self.centery-(self.sizey-1)/2 < 0 or self.centery + (self.sizey-1)/2 >= y):
            self.centery = random.randrange(0,y)
    def inRoom(self, xpos, ypos):
        if xpos <= self.centerx + (self.sizex-1)/2 and xpos >= self.centerx - (self.sizex-1)/2:
            if ypos <= self.centery + (self.sizey-1)/2 and ypos >= self.centery - (self.sizey-1)/2:
                return True
        return False
    def isWall(self, xpos, ypos):
        if xpos == self.centerx - (self.sizex-1)/2-1 or xpos == self.centerx + (self.sizex-1)/2+1:
            if ypos <= self.centery + (self.sizey-1)/2+1 and ypos >= self.centery - (self.sizey-1)/2-1:
                return True
        if ypos == self.centery - (self.sizey-1)/2-1 or ypos == self.centery + (self.sizey-1)/2+1:
            if xpos <= self.centerx + (self.sizex-1)/2 and xpos >= self.centerx - (self.sizex-1)/2:
                return True
        return False
            
            
x = floor(15,15,1)
x.create()
x.drawFloor()
