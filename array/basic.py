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
# print(first_negative_subarray(arr, len(arr),3))


#utilty fn
def remove_smaller_append_element(arr,element):
	arr2 = []
	#Remove every element smaller than current element prior to appending current element
	for idx,num in enumerate(arr):
		if num >= element:
			arr2.append(num)	#Could not pop smaller element in same list as iterating(check max_subarray with i/p-[3,2,1,5])

	arr2.append(element)
	return arr2

#sliding window problem
#find first max_subarray in subarray of size k

#i/p->[3,-5,1,6,-7,-10,9] , k = 3
#O/p -> 3,6,6,6,9

#i/p->[3,2,1,-1]
#o/p->3,2

def max_subarray(arr,n,k):
	i = 0 
	j = 0
	resultList = []
	demoList = []
	while j < n:
		element = arr[j]
		# print('here1:', element, demoList)
		demoList = remove_smaller_append_element(demoList,element)
		# print('here:', element, demoList)
		if j - i + 1 < k:
			j += 1
		else:
			#2. calculation
			res = demoList[0] 
			resultList.append(res)
			# print(i,j,res,resultList,demoList)
			#3. discard earlier calculation prior to window sliding
			if demoList[0] == arr[i]:
				demoList.pop(0)
			#4. slide window
			i += 1
			j += 1

			demoList.append
	return resultList

arr = [3,-5,1,6,-7,-10,9]
# arr = [3,-5,-1,6,-7,-10,9]
# arr = [3,2,1,-1]
# arr= [2,4,1,1]
# arr = [3,2,1,5]
arr = 2,7,5,4,8,3,1,2,-1,4
print(max_subarray(arr, len(arr),4))
