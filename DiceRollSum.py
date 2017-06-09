import math
#probability of rolling two dice and getting an 8
print("Enter a number. This program returns the probability that any given roll of two dice will sum add to that number.")
while 1:
	try:
		num = int(input(">>"))
		break
	except ValueError:
		print("I said a number.")	
n=0
for x in range(1,7):
	for y in range(1,7):
		if(x+y==num):
			n+=1
print(round(n/36*100,2),"%")			