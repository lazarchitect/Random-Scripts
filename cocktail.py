# cocktail shaker sort logic: interate through. compare a[i] to a[i+1]. if <, do nothing. if greater than, swap. when you get to the end, do it backwards.compare a[i] to a[i-1]. same actions.

from time import sleep 


def listIsSorted(a):
	for i in range(len(a)-1):
		if a[i]>a[i+1]:
			return False
	return True		
							
def cocktail(a):
	backwards = range(len(a)-1)[::-1]
	counter = 1
	while not (listIsSorted(a)):
		# print("Pass ",counter)
		counter+=1
		for i in range(len(a)-1):
			if a[i]>a[i+1]:
				temp = a[i]
				a[i] = a[i+1]
				a[i+1] = temp
				# print("swapped ",a[i]," and ", a[i+1])
				sleep(1)
				# print (a)
				sleep(1)
		if (listIsSorted(a)):
			break		
		for j in backwards:		
			if j!=0 and a[j-1]>a[j]:
				temp = a[j]
				a[j] = a[j-1]
				a[j-1] = temp
				# print("swapped ",a[j-1]," and ", a[j])
				sleep(1)
				# print (a)
				sleep(1)
	print("Your final answer: ")
	return a

a = [57,28,19,48]
print (cocktail(a))