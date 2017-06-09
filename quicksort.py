def q(a):
	if len(a)<2: return a
		#base case, also the best case efficiency. arrs of len 1 or 0 are sorted. O(n)
	m = sorted([a[0], a[int(len(a)/2)], a[len(a)-1]])[1]
		#getting a pivot. its recommended to get the median, and getting the median of the first, last, and middle is still good enough and more efficient.
		#m is the median of the first, last, and middle elements. this is useful for if the list is in worst-case, already sorted, or random, the pivot will act accordingly.
	return q([x for x in a if x<m]) + [x for x in a if x==m] + q([x for x in a if x>m])
		#RECOISHUN! the first item is calling quisksort on all the things less than or equal to the pivot, and the second is calling it on all the items greater than the pivot.  
	#Four O(n) things happening 2(log(n)) times. grand total of O(4n(2log(n))), or nlogn. Room for improvement here.

if __name__ == '__main__':
	import random
	array = [random.randint(1, 101) for i in range(int(input("How many items should be in the list?\n>> ")))]
	print("unsorted: "+str(array))
	print("sorted:   "+str(q(array)))

#codegolf. quicksort in 171 characters over 4 beautiful lines(I'm not counting main or comments). there's still room for improvement.