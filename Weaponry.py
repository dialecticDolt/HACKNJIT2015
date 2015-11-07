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
	agility = 1;

	def __init__(self):
		Weapon.__init__(self, self.damage, self.weaponRange, self.agility);

class longSword(Weapon):
	
	damage = 6;
	weaponRange = 3;
	agility = 3;
	
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




