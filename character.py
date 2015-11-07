import time
import random
class Character:

	#leagilistic attributes
	yPos = 0; #x position
	xPos = 0; #y position
	charID = time.time(); #get unique 11 digit timestamp as an id. hopefully they wont collide
	isAlive = False;

	#character attributes
	strength = 0;
	dexterity = 0;
	charisma = 0;
	luck = 0;
	intelligence = 0;
	wisdom = 0;
	constitution = 0;
	
	#combat related attributes
	health = 300; #default health	

	def __init__(self, xPos, yPos, isAlive):
		#assign legalistic attributes
		self.xPos = xPos
		self.yPos = yPos;
		self.isAlive = isAlive;

		#randomly generate char attributes
		self.strength = random.randint(1,10);
		self.dexterity = random.randint(1,10);
		self.charisma = random.randint(1,10);
		self.luck = random.randint(1,10);
		self.intelligence = random.randint(1,10);
		self.wisdom = random.randint(1,10);
		self.constitution = random.randint(1,10);

	def printAttr(self):
		#quickly prints all attributes
		print(self.strength);
		print(self.dexterity);
		print(self.luck);
		print(self.intelligence);
		print(self.wisdom);
		print(self.constitution);
#--------------------------------------------------------------------------------------------------------------------------------------
	#moving functions

	def getPositionX(self):
		return self.xPos;
	
	def getPositionY(self):
		return self.yPos;

	def moveLeftOne(self):
		self.xPos = self.xPos - 1;
	
	def moveRightOne(self):
		self.xPos = self.xPos + 1;

	def moveLeft(self, xUnits):
		self.xPos = self.xPos - xUnits;
	
	def moveRight(self, xUnits):
		self.xPos = self.xPos + xUnits;
	
	def setAxisX(self, X):
		self.xPos = X;	
	
	def moveUpOne(self):
		self.yPos = self.yPos + 1;
	
	def moveDownOne(self):
		self.yPos = self.yPos - 1;
	
	def moveUp(self, yUnits):
		self.yPos = self.yPos + yUnits;

	def moveDown(self, yUnits):
		self.yPos = self.yPos - yUnits;
	
	def setAxisY(self, Y):
		self.yPos = Y;
	
	def moveToLocation(self, x, y):
		self.xPos = x;
		self.yPos = y;
		
#-------------------------------------------------------------------------------------------------------------------------------------------	
x = Character(0,0,True);
x.printAttr();
		

