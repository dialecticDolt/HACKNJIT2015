import random
import sys
import math
import os
import time
import msvcrt

def kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = msvcrt.getch()
    else:
        ret = False
    return ret

class world:
    def __init__(self, floornum = 10, floorx = 100, floory = 35, minrooms = 8, maxrooms = 8):
        self.floornum = floornum
        self.floorx = floorx
        self.floory = floory
        self.floors = []
        for i in range(0, floornum):
            self.floors.append(floor(floorx, floory, random.randint(minrooms, maxrooms)))
            self.floors[i].create();

class character:
    def __init__(self, myWorld):
        while True:
            x = random.randint(0,myWorld.floorx)
            y = random.randint(0,myWorld.floory)
            if(myWorld.floors[0].inRoom(x,y)[1]):
                break
        myWorld.floors[0].remove(x,y)
        myWorld.floors[0].add(x,y,'@')
        self.xpos = x
        self.ypos = y
        self.myWorld = myWorld
        self.currentFloor = 0
    def moveUp(self):
        if (self.ypos+1 < self.myWorld.floory):
            if (self.myWorld.floors[self.currentFloor].movableSpace(self.xpos, self.ypos+1)):
                self.myWorld.floors[self.currentFloor].remove(self.xpos, self.ypos)
                self.myWorld.floors[self.currentFloor].add(self.xpos, self.ypos+1, '@')
                self.ypos = self.ypos + 1
    def moveDown(self):
        if (self.ypos-1 >= 0):
            if (self.myWorld.floors[self.currentFloor].movableSpace(self.xpos, self.ypos-1)):
                self.myWorld.floors[self.currentFloor].remove(self.xpos, self.ypos)
                self.myWorld.floors[self.currentFloor].add(self.xpos, self.ypos-1, '@')
                self.ypos = self.ypos - 1
    def moveLeft(self):
        if (self.xpos-1 >= 0):
            if (self.myWorld.floors[self.currentFloor].movableSpace(self.xpos-1, self.ypos)):
                self.myWorld.floors[self.currentFloor].remove(self.xpos, self.ypos)
                self.myWorld.floors[self.currentFloor].add(self.xpos-1, self.ypos, '@')
                self.xpos = self.xpos - 1
    def moveRight(self):
        if (self.xpos+1 < self.myWorld.floorx):
            if (self.myWorld.floors[self.currentFloor].movableSpace(self.xpos+1, self.ypos)):
                self.myWorld.floors[self.currentFloor].remove(self.xpos, self.ypos)
                self.myWorld.floors[self.currentFloor].add(self.xpos+1, self.ypos, '@')
                self.xpos = self.xpos + 1
    def update(self):
        self.myWorld.floors[self.currentFloor].drawFloor()

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
            if i >= 1:
                cont = False
                conf = False
                count = 0
                while not cont:
                    conf = False
                    temp = room()
                    temp.create(self.x, self.y)
                    count = count + 1
                    if count == 1000:
                        break
                    for j in range(0, i):
                        if temp.roomConflict(self.rooms[j]):
                            conf = True
                    cont = not conf
                    if not cont:
                        temp = None
                if not cont:
                    self.roomnum = i
                    break
            self.rooms.append(temp)
        for i in range(0, self.y):
            for j in range(0, self.x):
                if (self.inRoom(j,i)[1] == True):
                    (self.space)[i][j] = '.'
                elif self.isWall(j, i):
                    (self.space)[i][j] = '='
                else:
                    (self.space)[i][j] = ' '
        self.connect()
    def connect(self):
        self.hallways = []
        for i in range(1, self.roomnum):
            closestRoom = 0;
            distance = math.sqrt((self.rooms[i].centerx-self.rooms[0].centerx)**2+(self.rooms[i].centery-self.rooms[0].centery)**2)
            for j in range(1,i):
                if math.sqrt((self.rooms[i].centerx-self.rooms[j].centerx)**2+(self.rooms[i].centery-self.rooms[j].centery)**2) < distance:
                    closestRoom = j
                    distance = math.sqrt((self.rooms[i].centerx-self.rooms[j].centerx)**2+(self.rooms[i].centery-self.rooms[j].centery)**2)
            if abs(self.rooms[closestRoom].centerx - self.rooms[i].centerx) > abs(self.rooms[closestRoom].centery - self.rooms[i].centery):
                if self.rooms[closestRoom].centerx < self.rooms[i].centerx:
                    x2 = self.rooms[closestRoom].centerx + (self.rooms[closestRoom].sizex-1)/2+1
                    y2 = random.randint(self.rooms[closestRoom].centery - (self.rooms[closestRoom].sizey-1)/2, self.rooms[closestRoom].centery + (self.rooms[closestRoom].sizey-1)/2)
                    x1 = self.rooms[i].centerx - (self.rooms[i].sizex-1)/2-1
                    y1 = random.randint(self.rooms[i].centery - (self.rooms[i].sizey-1)/2, self.rooms[i].centery + (self.rooms[i].sizey-1)/2)
                    temp = self.pathFinding(x1, y1, x2, y2)
                    for n in temp:
                        self.hallways.append(n)
                        self.space[n[1]][n[0]] = '.'
                    for p in temp:
                        adj = [[p[0]+1,p[1]],[p[0]-1,p[1]],[p[0],p[1]+1],[p[0],p[1]-1],[p[0]+1,p[1]+1],[p[0]+1,p[1]-1],[p[0]-1,p[1]+1],[p[0]-1,p[1]-1]]
                        for n in adj:
                            if self.validSpace(n[0],n[1]):
                                self.space[n[1]][n[0]] = '='
                    ## door in right wall of closest room, in left wall of i
                else:
                    x2 = self.rooms[closestRoom].centerx - (self.rooms[closestRoom].sizex-1)/2-1
                    y2 = random.randint(self.rooms[closestRoom].centery - (self.rooms[closestRoom].sizey-1)/2, self.rooms[closestRoom].centery + (self.rooms[closestRoom].sizey-1)/2)
                    x1 = self.rooms[i].centerx + (self.rooms[i].sizex-1)/2+1
                    y1 = random.randint(self.rooms[i].centery - (self.rooms[i].sizey-1)/2, self.rooms[i].centery + (self.rooms[i].sizey-1)/2)
                    temp = self.pathFinding(x1, y1, x2, y2)
                    for n in temp:
                        self.hallways.append(n)
                        self.space[n[1]][n[0]] = '.'
                    for p in temp:
                        adj = [[p[0]+1,p[1]],[p[0]-1,p[1]],[p[0],p[1]+1],[p[0],p[1]-1],[p[0]+1,p[1]+1],[p[0]+1,p[1]-1],[p[0]-1,p[1]+1],[p[0]-1,p[1]-1]]
                        for n in adj:
                            if self.validSpace(n[0],n[1]):
                                self.space[n[1]][n[0]] = '='
                    ## door in left wall of closest room, in right wall of i
            else:
                if self.rooms[closestRoom].centery < self.rooms[i].centery:
                    x1 = random.randint(self.rooms[i].centerx - (self.rooms[i].sizex-1)/2, self.rooms[i].centerx + (self.rooms[i].sizex-1)/2)
                    y1 = self.rooms[i].centery - (self.rooms[i].sizey-1)/2-1
                    x2 = random.randint(self.rooms[closestRoom].centerx - (self.rooms[closestRoom].sizex-1)/2, self.rooms[closestRoom].centerx + (self.rooms[closestRoom].sizex-1)/2)
                    y2 = self.rooms[closestRoom].centery + (self.rooms[closestRoom].sizey-1)/2+1
                    temp = self.pathFinding(x1, y1, x2, y2)
                    for n in temp:
                        self.hallways.append(n)
                        self.space[n[1]][n[0]] = '.'
                    for p in temp:
                        adj = [[p[0]+1,p[1]],[p[0]-1,p[1]],[p[0],p[1]+1],[p[0],p[1]-1],[p[0]+1,p[1]+1],[p[0]+1,p[1]-1],[p[0]-1,p[1]+1],[p[0]-1,p[1]-1]]
                        for n in adj:
                            if self.validSpace(n[0],n[1]):
                                self.space[n[1]][n[0]] = '='
                    ## dorr in bottom wall of i, in upper wall of closest room
                else:
                    x1 = random.randint(self.rooms[i].centerx - (self.rooms[i].sizex-1)/2, self.rooms[i].centerx + (self.rooms[i].sizex-1)/2)
                    y1 = self.rooms[i].centery + (self.rooms[i].sizey-1)/2+1
                    x2 = random.randint(self.rooms[closestRoom].centerx - (self.rooms[closestRoom].sizex-1)/2, self.rooms[closestRoom].centerx + (self.rooms[closestRoom].sizex-1)/2)
                    y2 = self.rooms[closestRoom].centery - (self.rooms[closestRoom].sizey-1)/2-1
                    temp = self.pathFinding(x1, y1, x2, y2)
                    for n in temp:
                        self.hallways.append(n)
                        self.space[n[1]][n[0]] = '.'
                    for p in temp:
                        adj = [[p[0]+1,p[1]],[p[0]-1,p[1]],[p[0],p[1]+1],[p[0],p[1]-1],[p[0]+1,p[1]+1],[p[0]+1,p[1]-1],[p[0]-1,p[1]+1],[p[0]-1,p[1]-1]]
                        for n in adj:
                            if self.validSpace(n[0],n[1]):
                                self.space[n[1]][n[0]] = '='
                    ## door in upper wall of i, in bottom wall of closest room

    def pathFinding(self, x1, y1, x2, y2):
        ##return [[x1,y1],[x2,y2]]
        mainList = [[x2, y2]]
        while True:
            temp = self.pathFindingHelper(x1, y1, x2, y2);
            if temp[2] == False:
                mainList = [[temp[0],temp[1]]] +mainList;
                x2 = temp[0];
                y2 = temp[1];
            else:
                mainList = [[temp[0],temp[1]]]
                x2 = temp[0]
                y2 = temp[1]
            if x2 == x1 and y2 == y1:
                break
        return mainList
        
    def pathFindingHelper(self, x1, y1, x2, y2):
        mainList = [[x1,y1,0]]
        count = 1
        for n in mainList:
            temp = [[n[0]+1,n[1],count],[n[0]-1,n[1],count],[n[0],n[1]+1,count],[n[0],n[1]-1,count]]
            
            for i in temp:
                add = True
                if i[0] == x2 and i[1] == y2:
                    return [n[0],n[1],False]
                if not self.validSpace(i[0],i[1]):
                    if i[1] >= 0 and i[1] < self.y and i[0] >=0 and i[0] < self.x:
                        if self.space[i[1]][i[0]] == '=':
                            adj = [[i[0]+1,i[1]],[i[0]-1,i[1]],[i[0],i[1]+1],[i[0],i[1]-1]]
                            for x in adj:
                                if x in self.hallways:
                                    return [i[0],i[1],True]
                    add = False
                else:
                    for j in mainList:
                        if i[0] == j[0] and i[1] == j[1] and j[2] <= i[2]:
                            add = False
                if add:
                    mainList.append(i)
            count += 1
                        

    def validSpace(self, x, y):
        if y < 0 or y >= self.y:
            return False
        if x < 0 or x >= self.x:
            return False
        if self.space[y][x] == ' ':
            return True
        return False

    def movableSpace(self, x, y):
        if y < 0 or y >= self.y:
            return False
        if x < 0 or x >= self.x:
            return False
        if self.space[y][x] != '=':
            return True
        return False
            
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
    def add(self, x, y, thing):
        if len(thing) != 1:
            return -1
        self.space[y][x] = thing
    def remove(self, x, y, replace = '.'):
        self.space[y][x] = replace
    def drawFloor(self):
        os.system('cls')
        print '+'*((self.x)+2)
        for i in range(self.y-1, -1, -1):
            line = '+'
            for j in range (0, self.x):
                line += self.space[i][j]
            line += '+'
            print(line)
        print '+'*((self.x)+2)
            

class room:
    def __init__(self):
        self.sizex = random.randrange(1,8,2)
        self.sizey = random.randrange(1,8,2)
    def setSize(self, x, y):
        self.sizex = x
        self.sizey = y
    def setCenter(self, x, y):
        self.centerx = x
        self.centery = y
    def create(self, x, y):
        self.centerx = 0
        self.centery = 0
        while (self.centerx-(self.sizex-1)/2 < 1 or self.centerx + (self.sizex-1)/2 >= x-1):
            self.centerx = random.randrange(0,x)
        while (self.centery-(self.sizey-1)/2 < 1 or self.centery + (self.sizey-1)/2 >= y-1):
            self.centery = random.randrange(0,y)
    def roomConflict(self, room2):
        roomOneLeftEdge = self.centerx - (self.sizex-1)/2;
        roomOneRightEdge = self.centerx + (self.sizex-1)/2;
        roomOneTopEdge = self.centery + (self.sizey-1)/2;
        roomOneBotEdge = self.centery - (self.sizey-1)/2;
        
        roomTwoLeftEdge = room2.centerx - (room2.sizex-1)/2;
        roomTwoRightEdge = room2.centerx + (room2.sizex-1)/2;
        roomTwoTopEdge = room2.centery + (room2.sizey-1)/2;
        roomTwoBotEdge = room2.centery - (room2.sizey-1)/2;

        if roomTwoLeftEdge <= roomOneRightEdge+3 and roomTwoLeftEdge >= roomOneLeftEdge-3 and roomTwoTopEdge <= roomOneTopEdge+3 and roomTwoTopEdge >= roomOneBotEdge-3:
            return True
        if roomTwoLeftEdge <= roomOneRightEdge+3 and roomTwoLeftEdge >= roomOneLeftEdge-3 and roomTwoBotEdge <= roomOneTopEdge+3 and roomTwoBotEdge >= roomOneBotEdge-3:
            return True
        if roomTwoRightEdge <= roomOneRightEdge+3 and roomTwoRightEdge >= roomOneLeftEdge-3 and roomTwoTopEdge <= roomOneTopEdge+3 and roomTwoTopEdge >= roomOneBotEdge-3:
            return True
        if roomTwoRightEdge <= roomOneRightEdge+3 and roomTwoRightEdge >= roomOneLeftEdge-3 and roomTwoBotEdge <= roomOneTopEdge+3 and roomTwoBotEdge >= roomOneBotEdge-3:
            return True

        if roomOneLeftEdge <= roomTwoRightEdge+3 and roomOneLeftEdge >= roomTwoLeftEdge-3 and roomOneTopEdge <=roomTwoTopEdge+3 and roomOneTopEdge>= roomTwoBotEdge-3:
            return True
        if roomOneLeftEdge <= roomTwoRightEdge+3 and roomOneLeftEdge >= roomTwoLeftEdge-3 and roomOneBotEdge <=roomTwoTopEdge+3 and roomOneBotEdge>= roomTwoBotEdge-3:
            return True
        if roomOneRightEdge <= roomTwoRightEdge+3 and roomOneRightEdge >= roomTwoLeftEdge-3 and roomOneTopEdge <=roomTwoTopEdge+3 and roomOneTopEdge>= roomTwoBotEdge-3:
            return True
        if roomOneRightEdge <= roomTwoRightEdge+3 and roomOneRightEdge >= roomTwoLeftEdge-3 and roomOneBotEdge <=roomTwoTopEdge+3 and roomOneBotEdge>= roomTwoBotEdge-3:
            return True

        return False
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
            
random.seed(0)
x = world()
me = character(x)
x.floors[0].drawFloor()

while True:
    z = kbfunc()

    if z != False:
        if z.decode() == 'w':
            me.moveUp()
        if z.decode() == 's':
            me.moveDown()
        if z.decode() == 'a':
            me.moveLeft()
        if z.decode() == 'd':
            me.moveRight()
        me.update()
        
    #else:
        #time.sleep(0.1)

