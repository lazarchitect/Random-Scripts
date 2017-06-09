#implements a max heap, a tree structure where the root(the first item in the list) is always the largest.

def getHeight(index, array):
		L = len(array)
		total = 0
		while(index*2+1 < L):
			total+=1
			index = index*2+1
		return total	

class heap(object):
	
	array = []
	
	#constructor
	def __init__(self):
		pass
	
	#toString
	def printHeap(self):
		a = self.array
		
		i = 0
		levelup = 1
		level = 0
		
		while(i < len(a)):
			
			n = getHeight(i, self.array)
			#print(str(a[i]) + "'s height: "+str(n))
			if(n == 0):
				print(" "*2 + str(a[i]), end ="")
			else:
				print(" "*3*n + str(a[i]), end ="")
			
			if i-level==0:
				print()
				levelup *= 2
				level+=levelup
			
			i+=1
			
			
		print("\n")	#once at the end
	
	
	
	
	
	#other methods
	def insert(self, x):
		self.array.append(x)
		if(len(self.array) > 1):
			self.siftUp()
		
	def siftUp(self):
		sifter = len(self.array) - 1
		while(True):
			#compare sifter to its sibling, if it has one(if its an even index). 
				#if its smaller, break.
			if sifter%2==0:
				if(self.array[sifter] <= self.array[sifter - 1]):
					break
			#compare sifter to its parent, if its not at index 0.
				#if its smaller than its parent, break. 
				#else, swap it with its parent.
			if(self.array[sifter] <= self.array[int((sifter-1)/2)]):
				break
			else:
				(self.array[sifter], self.array[int((sifter-1)/2)]) = (self.array[int((sifter-1)/2)], self.array[sifter])
				sifter = int((sifter-1)/2)
			#make sifter have its new index and continue the loop.
			
		
	def delete(self):
		retval = self.array[0]
		self.array[0] = self.array[len(self.array) - 1]
		self.array.remove(self.array[len(self.array) - 1])
		self.siftDown()
		return retval
		
				
	def siftDown(self):
		a = self.array
		sifter = 0
		while(True):
			num = self.children(sifter)
			larger_child_index = -1234
			if(num == 0):
				break
			elif(num == 1):
				if(self.array[sifter*2 + 1] > self.array[sifter]):
					(self.array[sifter], self.array[sifter*2 + 1]) = (self.array[sifter*2 + 1], self.array[sifter])
				break
			else: #2 children
				if(a[sifter*2 + 1] > a[sifter*2 + 2]):
					larger_child_index = sifter*2 + 1
				else:
					larger_child_index = sifter*2 + 2
				if(a[larger_child_index] > a[sifter]):
					(a[sifter], a[larger_child_index]) = (a[larger_child_index], a[sifter])
				else:
					break	
			sifter = larger_child_index		
	
	def children(self, index):
		num = len(self.array)
		if index*2+2 < num:
			return 2
		if index*2+1 < num:
			return 1
		return 0
	
def heapsort(array):
	H = heap()
	for x in array:
		H.insert(x)
	retval = []
	for y in range(len(H.array)):
		retval.append(H.delete())	
	return retval	

arr = []		
print("welcome to heapsort. Insert each integer in the list, separated by <Enter>. Type something that's not a number to quit.")
while(True):
	try:
		arr.append(int(input(">>")))
	except ValueError:
		break
print(heapsort(arr))		
		
		
		
		
		
		