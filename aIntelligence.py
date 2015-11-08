import random
from Weaponry import *

class AI():
	
	startX = 0;
	startY = 0;
	xPos = 0;
	yPos = 0;
	weaponChoice = random.randint(1,6);
	weapon = None;
	health = 100;
	strength = 0;
	dexterity = 0;
	resolve = 0;

	def __init__(self, startX, startY, weaponChoice = 0, strength = 0, dexterity = 0, resolve = 0):

		self.startX = startX;
		self.startY = startY;
		self.xPos = self.startX;
		self.yPos = self.startY;
		self.strength = random.randint(1,10) if strength == 0 else strength;
		self.dexterity = random.randint(1,10) if dexterity == 0 else dexterity;
		self.resolve = random.randint(6,10) if resolve == 0 else resolve;

		self.weaponChoice = weaponChoice if weaponChoice > 0 else self.weaponChoice

		print(self.weaponChoice);	

		if(self.weaponChoice == 1):
			self.weapon = shortSword();
		elif(self.weaponChoice == 2):
			self.weapon = longSword();
		elif(self.weaponChoice == 3):
			self.weapon = Bow();
		elif(self.weaponChoice == 4):
			self.weapon = Mace();
		elif(self.weaponChoice == 5):
			self.weapon = Spear();
		elif(self.weaponChoice == 6):
			self.weapon = Dagger();

#---------------------------------------------------------------------------------------------------------------------------------------			

	def getPositionX(self):
		return self.xPos;

	def setPositionX(self, X):
		self.xPos = X;	

	def moveLeftOne(self):
		self.xPos = self.xPos - 1;
	
	def moveRightOne(self):
		self.xPos = self.xPos + 1;

	def moveLeft(self, xUnits):
		self.xPos = self.xPos - xUnits;
	
	def moveRight(self, xUnits):
		self.xPos = self.xPos + xUnits;

	def getPositionY(self):
		return self.yPos;

	def setPositionY(self, Y):
		self.yPos = Y;
	
	def moveUpOne(self):
		self.yPos = self.yPos + 1;
	
	def moveDownOne(self):
		self.yPos = self.yPos - 1;

	def moveUp(self, yUnits):
		self.yPos = self.yPos + yUnits;

	def moveDown(self, yUnits):
		self.yPos = self.yPos - yUnits;	
		
	def moveToLocation(self, x, y):
		self.xPos = x;
		self.yPos = y;

	def inRangeX(self, enemyPosX):
		differenceInPosition = self.xPos - enemyPosX;
		if(abs(differenceInPosition) <= self.weapon.rangeMod()):
			return True;
		else:
			return False;


	def inRangeY(self, enemyPosY):
		differenceInPosition = self.yPos - enemyPosY;
		if(abs(differenceInPosition) <= self.weapon.rangeMod()):
			return True;
		else:
			return False;

	def printRange(self):
		print(self.weapon.rangeMod());


#-----------------------------------------------------------------------------------------------------------------------------------------------
	def chaseEnemy(self, enemy):
		if(self.inRangeX(enemy.getPositionX()) and self.inRangeY(enemy.getPositionY())):
			enemy.damaged(self.weapon.weaponMod() * self.strength);

		else:
                        3+3
			#todo path to enenmy

	def shouldAttack(self, enemy):
		minimumExtraDistance = 3;

		#minimum extra distance is how close an emey will chase the character
		#depending on charisma level of character, changes extra distance
		if(enemy.charisma >= self.resolve):

			if(enemy.charisma == self.resolve):
				minimumExtraDistance = 2;

			elif(enemy.charisma == self.resolve + 1):
				minimumExtraDistance = 1;

			else:
				minimumExtraDistance = 0;

		

		if((enemy.getPositionX() <= self.weapon.rangeMod() + minimumExtraDistance) and (enemy.getPositionY() <= self.weapon.rangeMod() + minimumExtraDistance)):
			print("chasing")
			self.chaseEnemy(enemy);
		else:
                        3+3
			#todo path to return spot

			





			



