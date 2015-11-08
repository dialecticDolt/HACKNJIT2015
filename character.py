import time
import random
from Weaponry import * 
from aIntelligence import *

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

	def __init__(self, name, xPos, yPos, isAlive, strength = 0, dexterity = 0, charisma = 0, luck = 0, intelligence = 0, wisdom = 0):
		#assign legalistic attributes
		self.name = name;
		self.xPos = xPos
		self.yPos = yPos;
		self.isAlive = isAlive;
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


#----------------------------------------------------------------------------------------------------------------------------------		

		

	
	


x = Character("x",0,0,True);
y = AI(11,11);

y.shouldAttack(x);



		

