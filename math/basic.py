def find_missing(arr,n):
	actualTotal = sum(arr)
	n += 1 #add 1 as 1 element is missing
	expectedTotal = n*(n+1)/2
	return expectedTotal- actualTotal

arr = [4,5,1,2,6,3,8]
print(find_missing(arr,len(arr)))