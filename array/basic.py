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
print(max_sum_subarray(arr, len(arr),3))

