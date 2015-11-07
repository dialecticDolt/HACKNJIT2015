class Weapon:

	#default weapon is fists
	damage = 0; #damange 1-10, to be multiplied with strength
	weaponRange = 0; #range 1-10
	agility = 0; #agility 1-3: 1 being slow (encumbering), 2 being neutral, 3 being quick (speed bonus)

	def __init__(self, damage = 1, weaponRange = 1, agility = 2):
		self.damage = damage;
		self.weaponRange = weaponRange;
		self.agility = agility;
	
	def weaponMod(self):
		return self.damage;
	
	def rangeMod(self):
		return self.weaponRange;
	
	def speedMod(self):
		return self.agility;
	

class shortSword(Weapon):

	damage = 4;
	weaponRange = 2;
	agility = 3;

	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class longSword(Weapon):
	
	damage = 6;
	weaponRange = 3;
	agility = 1;
	
	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class Bow(Weapon):
	damage = 5;
	weaponRange = 10;
	agility = 2;

	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class Mace(Weapon):
	damage = 7;
	weaponRange = 2;
	agility = 1;

	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class Spear(Weapon):
	damage = 5;
	weaponRange = 4;
	agility = 1;

	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class Dagger(Weapon):
	damage = 3;
	weaponRange = 1;
	agility = 3;

	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class Armor():
	armorBonus = 0;
	armorCap = 100;

	def __init__(self):
		armorBonus = 0;
		armorCap = 100;
	
	def addArmor(self):
		if self.armorBonus < 0:
			self.armorBonus = 0;
		if self.armorBonus != self.armorCap:
			if(self.armorBonus >= self.armorCap-25):
				self.armorBonus = 100;
			else:
				self.armorBonus = self.armorBonus + 25;

	def damageArmor(self, damage):
		if self.armorBonus < 0:
			self.armorBonus = 0;
			
		self.armorBonus = self.armorBonus - damage;
		return (self.armorBonus > 0: 0 ? self.armorBonus);
	
	def getArmor(self):
		if self.armorBonus < 0:
			self.armorBonus = 0;
		return self.armorBonus;
			


