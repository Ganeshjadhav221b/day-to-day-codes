#sliding window problem
#find max sum subarray of size k
#i/p->[3,5,-1,6,7,-10,9]
#O/p -> max(7,10,12,3,6) -> 12

def max_sum_subarray(arr, n, k =3):
	i = 0
	j = 0
	maximum = -99
	subArrayTotal = 0
	while j < n:
		subArrayTotal += arr[j]
		# print(i,j,subArrayTotal)
		if (j - i + 1) < k:		#1. If window size isnt reached, keep incrementing j
			j += 1
		else:
			maximum = max(maximum, subArrayTotal) 		#2. perform calculation and store in variable 
			subArrayTotal -= arr[j-k+1]					#3. discard earlier calculation
			i += 1 										#4. shift window
			j += 1 	
		# print(i,j,subArrayTotal,maximum)
	return maximum
arr = [3,5,-1,6,7,-10,9]
# print(max_sum_subarray(arr, len(arr),3))


#sliding window problem
#find first negative in subarray of size k

#i/p->[3,-5,1,6,-7,-10,9] , k = 3
#O/p -> -5,-5, -7, -7,-7

#i/p->[3,-5,-1,6,-7,-10,9] , k = 3
#O/p -> -5,-5, -1,-7,-7


#i/p -> [3,5,7,-1,10]
#o/p ->None, -1, -1

#i/p -> [-3,5,7,1,10]
#o/p -> -3, None,None

def first_negative_subarray(arr, n, k=3):
	i = 0
	j = 0
	negativeList = []
	resultList = []
	while j < n:
		# print(i,j,subArrayTotal)

		element = arr[j]
		if element < 0:
			negativeList.append(element)
		if (j - i + 1) < k:		#1. If window size isnt reached, keep incrementing j
			j += 1
		else:
			#2. perform calculation and store in variable 
			res = negativeList[0] if len(negativeList)>0 else None
			resultList.append(res)
			# print(i,j,element,res,resultList)
			#3. discard earlier calculation
			if res == arr[i]:
				negativeList.pop(0)
			#4. shift window
			i += 1 
			j += 1
		# print('Here:',element, resultList, negativeList)
	return resultList
arr = [3,-5,1,6,-7,-10,9]
arr = [3,-5,-1,6,-7,-10,9]
arr = [3,5,7,-1,10]
arr = [-3,5,7,1,10]
print(first_negative_subarray(arr, len(arr),3))