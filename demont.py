import math
from random import shuffle
# you have a shuffled deck of cards labeled 1 through n. whats the chance that a card's label matches its index in the deck?
ans = 1 - 1/math.e
for n in range(int(input("start point?")),int(input("end point?"))):
	success = 0
	for d in range(100000):
		deck = [i for i in range(1,n+1)]#n+1
		shuffle(deck)
		j = 1
		for x in deck:
			if x == j:
				success+=1
				break
			j+=1
	print("success rate for",n,":",success/1000,"%")
print("What it should approach:",ans*100,"%")