import time
import random
from Weaponry import * 
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
	
	#combat related attributes
	health = 300; #default health	
	weapon = Weapon();
	armor = Armor();

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
		self.health = 300;

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

	
	

x = Character(0,0,True);
x.addArmor();
x.addArmor();
x.addArmor();
x.addArmor();
x.damaged(125);
print(x.getArmor());
print(x.getHealth());


		

