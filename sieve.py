def isPrime(sieve, number):
	for prime in sieve:
		if number%prime==0:
			return False #number is composite
	return True #number is prime!

def createSieve(n):
	number = 11
	sieve = [2, 3, 5, 7]
	while(len(sieve) < n):
		if(isPrime(sieve, number)): #for every i we go through, this method runs through all of sieve. the thing is, sieve will be fairly small for a while
			sieve.append(number)
		number+=2
	return sieve
	
if __name__ == '__main__':
	# from time import time
	print("an efficient algorithm to determine primes. enter a number n to print out the nth prime.")
	n = int(input(">>>"))
	# start = time()
	sieve = createSieve(n)
	# end = time()
	print("Nth Prime: "+str(sieve[n-1]))
	# print('time it took:' + str(round(end-start)))