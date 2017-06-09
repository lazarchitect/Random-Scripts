#python program that takes a string input thats a roman numeral and outputs the decimal value.

symbols = {"i":1, "v":5, "x":10, "d":500, "c":100, "l":50, "m":1000}
check = True

#method to verify the string is correct before we begin.
def invalid(s):
	
	#checks if the string has any non-numeral characters.
	for x in s:
		if x not in symbols:
			print("invalid character:",x)
			return True
	
	#checks if there are 4 1s, 10s, or 100s next to each other. This can be represented as the next 5-value minus one of them, and is therefore wrong. This one will be annoying.
	for index in range(len(s)):
		if(index<len(s)-3):
			char = s[index]
			if(char == "i" or char == "x" or char == "c"):
				if(char == s[index+1] and char == s[index+2] and char == s[index+3]):
					print("Invalid. 4 ",char.upper()+"s next to each other.")
					return True
			
			
			
		
	#checks if there are more than one of I, X, or C before a value larger than them. IIV and CCMC are not valid.
	for x in range(len(s)):
		if x > 1:
			if symbols[s[x-1]] < symbols[s[x]]:
				if symbols[s[x-1]] == symbols[s[x-2]]:
					print("Invalid format. Too many smaller values before a larger one.")
					return True
	
	#checks if the string has an increase in numeral value twice is a row. This is improper.
	check = False
	for x in range(len(s)):
		if x != len(s) - 1 and symbols[s[x]] < symbols[s[x+1]]: 
			if check:
				print("invalid number format. Too many increasing values in a row.")
				return True
			else: check = True
		else: check = False
	
	
	
	#Checks if there is a value right before its double. This is just that first value and is improper.
	for x in range(len(s)):
		if x!=len(s)-1 and symbols[s[x]]*2 == symbols[s[x+1]]:
			print("Invalid. "+s[x].upper()+" is right before its double.")
			return True
	
	#checks if there are two 5s, 50s, or 500s next to each other. This can represented by X, C, or M and therefore is invalid.
	for x in range(len(s)):
		if x!=len(s)-1 and (s[x] == "v" or s[x] == "d" or s[x] == "l") and s[x] == s[x+1]:
			print("invalid number format. Two or more",s[x].upper()+"'s right next to each other.")
			return True
	
	return False
	
def smallest(x, arr):
	for i in arr:
		if x > i:
			return False
	return True		

while(1):
	valz = []
	n = 0
	s = input("Enter a Roman Numeral, and the decimal number will be printed. Or, type \"quit\" to quit.\n>> ").lower()
	if(s == "quit"): break
	if(invalid(s)):
		continue
	prev = None
	total = 0
	for x in range(len(s)):
		char = s[x]
		toAdd = symbols[char]
		
		if prev != None:
			if symbols[prev] * 10 < toAdd:
				print("Invalid format. Decimal subtraction thing wrong.")
				check = False
				break
			
			toAdd -= symbols[prev] 
			if(not smallest(toAdd, valz)):
				print("Invalid")
				check = False
				break
			total += toAdd
			valz.append(toAdd)###################################
			#n = toAdd
			prev = None
			
		else:
			if x!=len(s)-1:
				if(symbols[s[x+1]] <= toAdd): 
					if(not smallest(toAdd, valz)):
						print("Invalid")
						check = False
						break
					total+=toAdd
					valz.append(toAdd)#########################
					n = toAdd
					prev = None
				
				else:
					prev = s[x]
			else:
				if(not smallest(toAdd, valz)):
					print("Invalid")
					check = False
					break
				total+=toAdd
				valz.append(toAdd)##################################
				n = toAdd
				break		
	if check: print(total)