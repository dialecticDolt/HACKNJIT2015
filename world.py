import random
import sys
import math
import os
import time
from Weaponry import *
from aIntelligence import *

import msvcrt

def kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = msvcrt.getch()
    else:
        ret = False
    return ret

class world:
    def __init__(self, floornum = 1, floorx = 100, floory = 35, minrooms = 8, maxrooms = 8):
        self.floornum = floornum
        self.floorx = floorx
        self.floory = floory
        self.floors = []
        for i in range(0, floornum):
            self.floors.append(floor(floorx, floory, random.randint(minrooms, maxrooms)))
            self.floors[i].create();

class Character:

    #leagilistic attributes
    name = "";
    yPos = 0; #x position
    xPos = 0; #y position
    charID = time.time();
    isAlive = False;

    #character attributes
    strength = 0;
    dexterity = 0;
    charisma = 0;
    luck = 0;
    intelligence = 0;
    wisdom = 0;

    #combat related attributes
    health = 300; #default health
    weapon = Weapon();
    armor = Armor();

    def __init__(self, name, isAlive, strength = 0, dexterity = 0, charisma = 0, luck = 0, intelligence = 0, wisdom = 0):
        #assign legalistic attributes
        self.name = name;
        while True:
            x = random.randint(0,NJIT.floorx)
            y = random.randint(0,NJIT.floory)
            if(NJIT.floors[0].inRoom(x,y)[1]):
                break
        NJIT.floors[0].add(x,y,'@')
        self.xpos = x
        self.ypos = y
        self.isAlive = isAlive;
        self.currentFloor = 0;
        self.charID = self.charID * reduce(lambda x, y: (x<<8)+ord(y), self.name, 0) #not really sure what this lamba does. it converts the name into a randomish number

        #randomly generate char attributes
        self.strength = random.randint(1,10) if strength == 0 else strength;
        self.dexterity = random.randint(1,10) if dexterity == 0 else dexterity;
        self.charisma = random.randint(1,10) if charisma == 0 else charisma;
        self.luck = random.randint(1,10) if luck == 0 else luck;
        self.intelligence = random.randint(1,10) if intelligence == 0 else intelligence;
        self.wisdom = random.randint(1,10) if wisdom == 0 else wisdom;
        self.health = 300;

    def printAttr(self):
        #quickly prints all attributes
        print(self.strength);
        print(self.dexterity);
        print(self.charisma);
        print(self.luck);
        print(self.intelligence);
        print(self.wisdom);
#--------------------------------------------------------------------------------------------------------------------------------------
    #moving functions

    def moveUp(self):
        if (self.ypos+1 < NJIT.floory):
            if (NJIT.floors[self.currentFloor].movableSpace(self.xpos, self.ypos+1)):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos, self.ypos+1, '@')
                self.ypos = self.ypos + 1
    def moveDown(self):
        if (self.ypos-1 >= 0):
            if (NJIT.floors[self.currentFloor].movableSpace(self.xpos, self.ypos-1)):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos, self.ypos-1, '@')
                self.ypos = self.ypos - 1
    def moveLeft(self):
        if (self.xpos-1 >= 0):
            if (NJIT.floors[self.currentFloor].movableSpace(self.xpos-1, self.ypos)):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos-1, self.ypos, '@')
                self.xpos = self.xpos - 1
    def moveRight(self):
        if (self.xpos+1 < NJIT.floorx):
            if (NJIT.floors[self.currentFloor].movableSpace(self.xpos+1, self.ypos)):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos+1, self.ypos, '@')
                self.xpos = self.xpos + 1
    def update(self):
        NJIT.floors[self.currentFloor].drawFloor()


    def getPositionX(self):
        return self.xpos;

    def setPositionX(self, X):
        if X >= 0 and X <NJIT.floorx:
            if NJIT.floors[self.currentFloor].movableSpace(X, self.ypos):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(X, self.ypos, '@')
                self.xpos = X;

    def moveLeftMany(self, xUnits):
            if self.xpos - xUnits >= 0:
                    if (NJIT.floors[self.currentFloor].movableSpace(self.xpos - xUnits, self.ypos)):
                            NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                            NJIT.floors[self.currentFloor].add(self.xpos - xUnits, self.ypos, '@')
                            self.xpos = self.xpos - xUnits;

    def moveRightMany(self, xUnits):
        if self.xpos + xUnits < NJIT.floorx:
            if NJIT.movableSpace(self.xpos + xUnits, self.ypos):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos + xUnits, self.ypos, '@')
                self.xpos = self.xpos + xUnits;

    ###

    def getPositionY(self):
        return self.ypos;

    def setPositionY(self, Y):
        if Y >= 0 and Y < NJIT.floory:
            if NJIT.movableSpace(self.xpos, Y):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos, Y, '@')
                self.ypos = Y;

    def moveUpMany(self, yUnits):
        if self.ypos + yUnits < NJIT.floory:
            if NJIT.movableSpace(self.xpos, self.ypos + yUnits):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos, self.ypos + yUnits)
                self.ypos = self.ypos + yUnits;

    def moveDownMany(self, yUnits):
        if self.ypos - yUnits >= 0:

            if NJIT.movableSpace(self.xpos, self.ypos - yUnits):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos, self.ypos - yUnits)
                self.ypos = self.ypos - yUnits;


            if NJIT.movableSpace(self.xpos, self.ypos - yUnits):
                NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                NJIT.floors[self.currentFloor].add(self.xpos, self.ypos - yUnits)
                self.ypos = self.ypos - yUnits;


    def moveToLocation(self, x, y):
        if x >= 0 and x < NJIT.floorx:
            if y >= 0 and y < NJIT.floory:
                if NJIT.movableSpace(x,y):
                    NJIT.floors[self.currentFloor].remove(self.xpos, self.ypos)
                    NJIT.floors[self.currentFloor].add(x,y,'@')
                    self.xpos = x;
                    self.ypos = y;

#-------------------------------------------------------------------------------------------------------------------------------------------
    #weapon stuff

    def pickUpWeapon(self,newWeapon):
        self.weapon = newWeapon

    def dropWeapon(self):
        self.weapon = Weapon();


    def attack(self):
        return self.strength*self.weapon.weaponMod();

    def attackSpeed(self):
        #attackSpeed will be 1-30.
        #dexterity and weapon agility play a role. This is essentially a measure of how fast one can attack
        return self.dexterity*self.weapon.speedMod();

    def attackRange(self):
        return self.weapon.rangeMod();

    def damaged(self, damageTaken):
        self.health = self.health + self.armor.damageArmor(damageTaken); #only returns a value if damage exceeds armor. that value should always be negative


    def heal(self, damageHealed):
        self.health = self.health + damagedHealed;

    def getHealth(self):
        return self.health;

    def getArmor(self):
        return self.armor.getArmor();

    def addArmor(self):
        self.armor.addArmor();

    def changeStrength(self, strAdd):
        self.strength = self.strength + strAdd;

    def changeDexterity(self, dexAdd):
        self.dexterity = self.dexterity + dexAdd;

    def changeCharisma(self, charAdd):
        self.charisma = self.charisma + charAdd;

    def changeLuck(self, luckAdd):
        self.luck = self.luck + luckAdd;

    def changeIntelligence(self, intAdd):
        self.intelligence = self.intelligence + intAdd;

    def changeWisdom(self, wisAdd):
        self.wisdom = self.wisdom + wisAdd;

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
        if self.space[y][x] == 'E' or self.space[y][x] == '@':
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
NJIT = world()
