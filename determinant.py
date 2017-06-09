#given an n by n matrix, this algorithm finds its determinant.

matrix1 = [[4]]
matrix2 = [[1,2],[3,4]]
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
matrix4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrixbad = [[45,4]]

def invalid(matrix):#should return false if the parameter is totally a wrong type, does not contain numbers, or is not square
	try:
		x = len(matrix)
		for i in matrix:
			if len(i) != x: 
				print("WAT")
				return True
			for j in i:
				if not isinstance(j, int) and not isinstance(j, float): 
					print("WAT2")
					return True	
		return False
	except:
		print("WAT3")
		return True

def submatrix(matrix, index):
	sub = []
	for i in range(1, len(matrix)):
		sub.append([])
		for j in range(len(matrix[i])):
			if j == index: continue
			x = matrix[i][j]
			sub[i-1].append(x)
	return sub
	
#should be recursive with base case of n=1?
def determinant(matrix): #assuming a valid 2D matrix input.
	if(invalid(matrix)): return "bad matrix input"
	if isinstance(matrix, int): return matrix
	n = len(matrix)
	if n == 1:
		return matrix[0][0]
	if n == 2:
		return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
	else:
		total = 0
		index = 0
		for currValIndex in range(len(matrix[0])):
			index+=1
			determ = determinant(submatrix(matrix, index-1))
			if currValIndex%2 == 1: determ*=-1
			print(matrix,matrix[0][currValIndex]*determ)
			total += matrix[0][currValIndex]*determ
		return total
		
if __name__ == "__main__":
	x = int(input("Enter a number>>"))
	if x == 1: print(determinant(matrix1))
	elif x == 2: print(determinant(matrix2))
	elif x == 3: print(determinant(matrix3))
	elif x == 4: print(determinant(matrix4))
	elif x == 5: print(determinant(matrixbad))
	else: print("too large")