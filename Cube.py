#NSEW
#improvements: make it based on real time and give people 5-6 minutes. 5:40? would make it more stressful but probably easier.
	#randomize lever location... oh god
#problems: trying to go from room 7 or room 9 to room 8 sometimes doesnt work, and after several tries warps you to room 5. like what	
def youWin():
	print("You've escaped! Congratulations, you're free!")
	return;
def nIncrement(n):
	
	if(n==20):
		print("You ran out of time! the walls slowly close in...")
		print("YOU LOSE")
		print("Run cube.py to try again.")
		return True;
	if(n>15):
		print("A frantic beeping emanating from below you urges you to hurry. You fear that the timer is approaching zero.")	
	return False;	 

def go(cmd, directions):
	cmd = cmd.lower()
	if(cmd=="quit"):
		print("Quitters never win.")
		quit()
	if cmd=="n" or cmd=="north":
		if(directions[0]):
			return 0
		else:
			cmd = input("Can't go that way. There's a wall there. Which way would you go?  >").lower()
			return go(cmd, directions)
	elif cmd=="s" or cmd=="south":
		if(directions[1]):
			return 1
		else:
			cmd = input("Can't go that way. There's a wall there. Which way would you go?  >").lower()
			return go(cmd, directions)
	elif cmd=="e" or cmd=="east":
		if(directions[2]):
			return 2
		else:
			cmd = input("Can't go that way. There's a wall there. Which way would you go?  >").lower()
			return go(cmd, directions)
	elif cmd=="w" or cmd=="west":	
		if(directions[3]):
			return 3
		else:
			cmd = input("Can't go that way. There's a wall there. Which way would you go?  >").lower()
			return go(cmd, directions)
	cmd = input("That doesn't make sense. Which way would you go?  >").lower()
	return go(cmd, directions)




				

def room1(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	directions = [False,True,True,False]
	print("\nThis room is a corner. There are only two ways out, south and east. In here lies a lever with three large red dots on it.")
	if(levers[2]):
		print("the lever is thrown.")
	else:	
		switch = input("do you want to pull this lever? \"yes\" or\"no\".").lower()
		if(switch=="yes"):
			if levers[0] and levers[1]:
				levers[2]=True
				print("The lever slides into place and you can hear more grinding in the walls.")
			else:
				print("The lever won't budge. Good try though.")	
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==1:
			room4(n, levers);
			break
		elif(go(cmd, directions))==2:
			room2(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")


def room2(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	print("\nyou're in the room with the timer. it reads "+str(20-n)+":00. To the south, east, and west are rooms identical to this one.")
	directions = [False, True, True, True]
	cmd = input("Which way would you go?   >")
	while(True):	
		if(go(cmd, directions))==1:
			room5(n, levers);
			break
		elif(go(cmd, directions))==2:
			room3(n, levers);
			break
		elif(go(cmd, directions))==3:
			room1(n, levers);
			break
		else:
			cmd = input("Can't go that way. Which way would you go?   >")	
			
def room3(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	#passages to the west and south, nothing else
	print("\nIt seems you've hit a corner: There are only passages to the west and south. Nothing is in this room.")
	directions = [False,True,False,True]
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==1:
			room6(n, levers);
			break
		elif(go(cmd, directions))==3:
			room2(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")	
			
def room4(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	directions = [True,True,True,False]
	print("\nThis room has three exits. Corridors lie to the north, south and east. There's another lever here, this time with four large dots.")
	if(levers[3]):
		print("the lever is thrown.")
	else:	
		switch = input("do you want to pull this lever? \"yes\" or\"no\".").lower()
		if(switch=="yes"):
			if levers[0] and levers[1] and levers[2]:
				levers[3]=True
				print("With some resistance, the lever slides roughly into place, and immediately the walls vibrate intensely for a few seconds.")
			else:
				print("The lever won't budge, and you pushed really hard, too.")	
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==0:
			room1(n, levers);
			break
		elif(go(cmd, directions))==1:
			room7(n, levers);
			break	
		elif(go(cmd, directions))==2:
			room5(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")			
				
def room5(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	print("\nFrom this room, identical rooms can be seen in all directions. In here is a machine with a lever and a large red dot on it.")
	if(levers[0]):
		print("the lever is in its on position.")
	else:	
		switch = input("do you want to flip the lever? \"yes\" or \"no\".  >").lower()
		if(switch=="yes"):
			print("you throw the lever. somewhere, gears can be heard grinding, and the walls vibrate ever so slightly.")
			levers[0] = not levers[0]
	directions = [True,True,True,True]
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==0:
			room2(n, levers);
			break
		elif(go(cmd, directions))==1:
			room8(n, levers);
			break
		elif(go(cmd, directions))==2:
			room6(n, levers);
			break
		elif(go(cmd, directions))==3:
			room4(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")			
			
def room6(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	#exits to the north, south, and west
	directions = [True, True, False, True]
	print("\nYet again, you can see more identical pathways leading away in cardinal directions. This time, they lie to the north, south, and west. This room is otherwise vacant and barren.")
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==0:
			room3(n, levers);
			break
		elif(go(cmd, directions))==1:
			room9(n, levers);
			break	
		elif(go(cmd, directions))==3:
			room5(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")						
		
def room7(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	#exits to the north and east
	directions = [True, False, True, False]
	print("\nA corner room. Exits to the north and east. Nothing much to see or do here.")
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==0:
			room4(n, levers);
			break	
		elif(go(cmd, directions))==2:
			room8(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")				
			
def room8(n, levers):
	directions = [True,False,True,True]
	n+=1;
	if nIncrement(n):
		return;
	print("\nRooms can be seen to the east, west, and north. In this room there's another timer. It reads",str(20-n)+":00. There's also a large panel in the wall. Next to it is a triangle of little dots.")
	if(levers[0]):
		print("the dot at the top of the triangle is lit up.")
	if(levers[1]):
		print("the dots just below the top of the triangle are lit up.")
	if(levers[2]):
		print("the dots below that are lit up as well.")		
	if(levers[3]):
		print("The bottom row of dots are similarly lit up.")
		directions[1]=True	
	if directions[1]:
		print("The panel has moved aside to reveal a brightly lit tunnel to the south.")	
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==0:
			room5(n, levers);
			break
		elif(go(cmd, directions))==1:
			youWin();
			break
		elif(go(cmd, directions))==2:
			room9(n, levers);
			break
		elif(go(cmd, directions))==3:
			room7(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")		
			
def room9(n, levers):
	n+=1;
	if nIncrement(n):
		return;
	#lever number 2, and exits to the north and west		
	directions = [True, False, False, True]
	print("\nA corner room. Exits to the north and west. There's a lever with two large red dots on it, just sitting there.")
	if(levers[1]):
		print("the lever is thrown.")
	else:	
		switch = input("do you want to pull this lever? \"yes\" or\"no\".").lower()
		if(switch=="yes"):
			if levers[0]:
				levers[1]=True
				print("The lever slides roughly into place. The walls groan and rust chips off onto your hands.")
			else:
				print("The lever won't budge, despite your best efforts.")	
	cmd = input("Which way would you go?  >")
	while(True):	
		if(go(cmd, directions))==0:
			room6(n, levers);
			break	
		elif(go(cmd, directions))==3:
			room8(n, levers);
			break	
		else:
			cmd = input("Can't go that way. Which way would you go?  >")					

	
########################################################################################################GAME START




print("\nyou wake up to find yourself in a cubic room, whitewashed and bare, staring at a huge countdown timer. The timer is at 20:00, and steadily counting down. You wonder what happens when it hits zero; considering you have no idea where you are, you decide you'd rather not find out. Let's get outta here! (You can move in cardinal directions, ex. n or north to go north. quit ends the game.)\n")

"""
| 1 | 2 | 3 |     start at 2. end at 8.
| 4 | 5 | 6 |     2 has the timer. 8 has another timer and the exit.
| 7 | 8 | 9 |	  5 has the one-dot. 9 has the two-dot. 1 has the three-dot. 4 has the four-dot. All other rooms are empty.
"""
levers = [False, False, False, False]
n = -1
room2(n, levers);