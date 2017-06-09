class Bus(object):

	condition = "New"
	timesDriven = 0

	def __init__(self, color):#constructor
		self.color = color

	def printBus(self):
		print("this is a bus. it is in "+self.condition+" condition.")

	def setcolor(self, color):#setter
		self.color = color
		print("New paint job time! Your bus is now ",self.color)

	def drive(self):
		self.timesDriven+=1
		if (self.timesDriven==1):
			self.condition = "Like New"
		elif (self.timesDriven==2):
			self.condition="Slightly Used"
		elif (self.timesDriven==3):
			self.condition="Used"
		elif (self.timesDriven==4):
			self.condition="Very Used"
		else:
			self.condition="Old"
#main
GreyHound = Bus("Red")

GreyHound.setcolor("Blue")

GreyHound.drive()
GreyHound.drive()

print(GreyHound.timesDriven)

GreyHound.drive()

GreyHound.printBus()