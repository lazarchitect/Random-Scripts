class atom():
	#fields
	
	def valences(self):
		if self.shells == 1:
			return self.electrons
		if self.shells == 2:
			return self.electrons - 2
		if self.shells == 3:
			return self.electrons - 10
		if self.shells == 1:
			return self.electrons - 28
		if self.shells == 1:
			return self.electrons - 50
		#no higher					
	
	def shellLevel(self):
		temp = self.electrons
		if temp<3:
			return 1
		if temp<11:
			return 2
		if temp<29:
			return 3
		if temp<51:
			return 4
		#I will not be working with atoms larger than this
	
	#constructor
	def __init__(self, protons, electrons, neutrons):
		self.protons = protons
		self.electrons = electrons
		self.number = protons
		self.weight = protons + neutrons
		self.shells = self.shellLevel()
		self.valence = self.valences()
		
	
	#toString is just str()
		
	#other methods
	
		
if(__name__ == "__main__"):
	N = atom(7,7,7)	
	print(N.shells)
	print(N.valence)