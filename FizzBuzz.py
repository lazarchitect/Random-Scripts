"""Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."""

#String assignment and concatentation method
for x in range(1,101):
	f = ""
	b = ""
	if(x%3==0):
		f = "Fizz"
	if(x%5==0):
		b = "Buzz"	
	if(f+b == ""):
		print(x)
		continue
	print(f+b)	

#simple if/else check method	
for x in range(1,101):	
	if x%3==0 and x%5==0:
		print("FizzBuzz")
	elif x%3==0:
		print("Fizz")
	elif x%5==0:
		print("Buzz")
	else:
		print(x)