n = 6

def recursive_fib(n):
	if n == 0 or n == 1:
		return n

	res = recursive_fib(n-1)+recursive_fib(n-2)
	#print(res)
	return res


def memoized_fib(n , seen):
	if n == 0 or n == 1:
		#print(n)
		return n
	if seen[n] == 0:
		res = memoized_fib(n-1,seen) + memoized_fib(n-2,seen)
		seen[n] = res
	else:
		res = seen[n]

	#print(res, seen)
	return res

# print(recursive_fib(n))
# print(memoized_fib(n, [0]*(n+1)))


#@ each stair, allowed to climb 1,2,3 steps per move
#0 steps -> 1
#1 steps -> 1
#2 steps -> 2 (0->2, 0->1->2)
#3 steps -> 4 (0->1->2->3, 0->1->3, 0->2->3, 0->3)
#4 steps -> 7 (0->1->2->3->4, 0->1->2->4, 0->1->3->4, 0->2->3->4, 0->1->4, 0->2->4, 0->3->4)
#5 steps -> 13 (0->1->2->3->4->5 [1 step per move-> 1]
# 				0->1->2->3->5, 0->1->2->4->5, 0->1->3->4->5, 0->2->3->4->5 [a 2 steps move ->4]
#				0->3->4->5, 0->2->4->5, 0->2->3->5, 0->1->4->5, 0->1->3->5, 0->1->2->5 [a 3 step move ->6]
#				0->3->5 [a 2 + a 3 step move ->1]
#				0->1->5,  0->2->5, [one intermediate step ->4] #Ignore
#				0->5) [1]  #Ignore
#				total = 1+4+6+1 = 12
def recursive_climbing_stairs(n):
	if n == 0:
		return 1
	if n < 3:
		return n
	return recursive_climbing_stairs(n-1)+recursive_climbing_stairs(n-2)+recursive_climbing_stairs(n-3) 

def memoized_climbing_stairs(n, seen):
	if n == 0:
		return 1
	if n < 3:
		return n
	if seen[n] == 0:
		res = memoized_climbing_stairs(n-1,seen)+memoized_climbing_stairs(n-2,seen)+memoized_climbing_stairs(n-3,seen) 
		seen[n] = res
	else:
		res = seen[n]

	return res


n=5

# print(recursive_climbing_stairs(n))
# print(memoized_climbing_stairs(n,[0]*(n+1)))

#lets say each stair has energy value associated, and only those max. jumps can be done
#idea is to find the number of ways to reach top
#ex-
#arr =[3,3,0,2,2,3]
#dp = [8,5,0,3,2,1,1]
#maintain an array where each element indicates ways to reach end.
#start from right, as at last step 
#dp[1] = dp[2]+dp[2]+dp[4](next 3 elements because arr[1] = 3)
#dp[4] = dp[5]+dp[6](next 2 elements because arr[4] = 2)
def tabulation_climbing_stairs_with_jumps(n,arr):
	dp = [0]*(n+1)
	dp[n] = 1

	for i in range(n-1,-1,-1):
		for j in range(i+1,i+arr[i]+1):
			if j>=len(dp):
				break
			# print(i,j,i+arr[i],dp)
			dp[i] += dp[j]
	return dp[0]
arr =[3,3,0,2,2,3]

#print(tabulation_climbing_stairs_with_jumps(len(arr),arr))



#arr= [3,2,4,2,0,2,3,1,2,2]
#dp = [4,3,4,None,0,3,2,2,1,1,0]
#start from right
#each  element in dp says least jumps to reach end
#
#
def tabulation_minimum_jumps_to_end(n,arr):
	dp = [None]*(n+1)
	dp[n] = 0
	for i in range(n-1,-1,-1):
		minimum = 999
		for j in range(i+1,i+arr[i]+1):
			if j>=len(dp):
				break
			if dp[j] != None:
				minimum = min(minimum,dp[j])
			if minimum != 999:
				dp[i] = minimum + 1 
			print(i,j,minimum,dp)
	return dp[0]

arr = [3,2,4,2,0,2,3,1,2,2]
# print(tabulation_minimum_jumps_to_end(len(arr),arr))



#Given 2d matrix where each element represent cost to jump to next step[any direction](only 1 step could be jumped though)
#Aim to find minimum cost to reach bottom right(exit) from top left(start)
#[2*,3*,4,1]
#[6,3*,8,1]
#[1,1*,0*,3*]
#[6,7,4,2*]
#*indicate optimal path taken
#Maintain array ->DP which indicates minimum cost from that step until destination
#Start from bottom right, work way right-upward
#[14,12,11,7]
#[13,9,13,6]
#[7,6,5,5]
#[19,13,6,2]

def tabulation_mimnimum_cost_path(matrix, m, n):
	maximum = 999  #constant
	right = maximum #temporary initialization
	below = maximum #temporary initialization
	dp = [[maximum for i in range(m)] for j in range(n)]
	dp[m-1][n-1] = matrix[m-1][n-1]
	for i in range(m-1,-1,-1):
		for j in range(n-1,-1,-1):
			if i == m-1 and j == n-1:
				continue
			belowIndex = i + 1
			rightIndex = j + 1
			if belowIndex < m:
				below = dp[belowIndex][j]

			if rightIndex < n:
				right = dp[i][rightIndex]
			 
			dp[i][j] = min(right,below) + matrix[i][j]
			# print(i,j,rightIndex,right, belowIndex, below, matrix[i][j],dp[i][j] )
			print(dp)
	return dp[0][0]

matrix = [[2,3,4,1],[6,3,8,1],[1,1,0,3],[6,7,4,2]]
# print(tabulation_mimnimum_cost_path(matrix, len(matrix), len(matrix[0])))


def flood_fill():
	pass



#consider 2d matrix
#0 0 1
#1 0 0
#0 0 0
#print ways to reach right bottom point(target) from top right(source)
#above example- rdrd, rddr
#Start with top right, check all directions
def maze_path(matrix, m, n, i,j,path_so_far):
	if i == m or j == m or matrix[i][j] == 1:
		return
	if i == m-1 and j == n-1:
		print(path_so_far)
		return
	# print(i,j,m,n,path_so_far)
	maze_path(matrix, len(matrix), len(matrix[0]),i+1,j,path_so_far+"d")
	maze_path(matrix, len(matrix), len(matrix[0]),i,j+1,path_so_far+"r")
	

matrix = [[0,0,1],[1,0,0],[0,0,0]]
# maze_path(matrix, len(matrix), len(matrix[0]),0,0,"")

#NOTE: Next 4 problems are related.
#Given lets say 3 coins with limited supply(no duplicates)->
#2,3,5
#find if we can for target sum, example 7
#Here answer should be true for 7 target, false for 9

#maintain x*y dp matrix, where x = number of elements, y = target sum
#we need 2d because otherwise 2,6 would be set to 1 in this case.

# (index)element| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |  
# (0)-          | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  
# (1)2    		| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  
# (2)3    		| 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |  0 |  
# (3)5    		| 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |  1 | 
def target_subset_sum(arr, n, target):
	cols = target+1
	rows = n+1
	dp = [[0 for i in range(cols)] for j in range(rows)]
	for i in range(rows):
		dp[i][0] = 1
	for i in range(1,rows):
		for j in range(1,cols):
			aboveIndex = i-1
			withOtherIndex = j-arr[i-1]
			above = 0
			withOther = 0
			
			if aboveIndex >= 0:
				above = dp[aboveIndex][j] 
			if withOtherIndex >= 0:				#i>0 check not needed, otherwise declare 1 more extra row.
				withOther = dp[i-1][withOtherIndex]
			
			dp[i][j] = max(above, withOther)
			# print(i,j,arr[i],aboveIndex, withOtherIndex, int(arr[i] == j), above, withOther, dp)
	print(dp)
	return dp[n][target]

arr = [2,3,5]
# print(target_subset_sum(arr, len(arr), 10))

#Given lets say 3 coins with limited supply->
#2,3,5
#find number of ways to acheive target sum, example 7
#Here answer should for 7 target be 2->(2,5), (2,3,2) 

#maintain x*y dp matrix, where x = number of elements, y = target sum

# index| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |  
# -    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 | 
# 2    | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  
# 3    | 1 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 0 |  0 |  
# 5    | 1 | 0 | 1 | 1 | 0 | 2 | 0 | 2 | 2 | 0 |  3 | 
def target_subset_sum(arr, n, target):
	cols = target+1
	rows = n + 1
	dp = [[0 for i in range(cols)] for j in range(rows)]
	for i in range(rows):
		dp[i][0] = 1
	for i in range(1, rows):
		for j in range(1, cols):
			withOtherIndex = j-arr[i-1]
			above = dp[i-1][j] if i >= 1 else 0
			withOther = 0
			if withOtherIndex >= 0:
				withOther = dp[i-1][withOtherIndex] 
				if withOther>0 and withOtherIndex > 0:
					withOther +=  1    #if its not same element, then its being added (example - 1,5)
			dp[i][j] = max(above, withOther) #+ int(arr[i] == j)
			# print(i,j,arr[i],aboveIndex, withOtherIndex, int(arr[i] == j), above, withOther)
	print(dp)
	return dp[n][target]

# print(target_subset_sum(arr, len(arr), 10))




#Given lets say 3 coins with infinite supply->
#2,3,5
#find minimum number of ways to acheive target sum, example 7
#Here answer should for 7 target be 2->(2,5), (2,3,2) 
#For target 10 answer would be 4 -> (2,2,2,2),(5,5),(2,2,3,3),(2,3,5)
#maintain dp array, with length = target sum

# iteration(0)| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |  
# 2  		  | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |  1 |  
# 3    		  | 1 | 0 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 |  2 |  
# 5    		  | 1 | 0 | 1 | 1 | 0 | 2 | 2 | 2 | 3 | 3 |  4 | 

def coin_change_combination(coins, n, target):
	length = target+1
	dp = [0 for i in range(length)]
	dp[0] = 1
	for coin in coins:
		for j in range(length):
			withOtherIndex = j-coin
			dp[j] +=  dp[withOtherIndex] if withOtherIndex >= 0 else 0
		
		# print(i,j,withOtherIndex,dp)
	return dp[target]
# print(coin_change_combination(arr, len(arr), 10))

#Given lets say 3 coins with infinite supply->
#2,3,5
#Here answer should for 7 target be 5->(2,5), (5,2), (2,2,3), (2,3,2), (3,2,2)


# iteration(0)| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |  
# 2  		  | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |  1 |  
# 3    		  | 1 |	 0 | 1 | 1 | 1 | 2 | 2 | 3 | 4 | x |  x |  
# 5    		  | 1 | 0 | 1 | 1 | 0 | 3 | 2 | 2 | 3 | 3 |  4 | 

def coin_change_permutation(coins, n, target):
	length = target+1
	dp = [0 for i in range(length)]
	dp[0] = 1
	for i in range(length):
		for coin in coins:
			dp[i] += dp[i-coin] if i >= coin else 0
	print(dp)

	return dp[target]

# print(coin_change_permutation(arr, len(arr), 5))


def longest_common_subsequence(s1,s2,n1,n2):
	rows = n1+1
	cols = n2+1
	dp = [[0 for i in range(cols)] for j in range(rows)]
	for i in range(1,rows):
		for j in range(1,cols):
			if s1[i-1] == s2[j-1]:   #if match, add 1 to top-left diag. element
				dp[i][j] = dp[i-1][j-1] + 1
			else:				#if not match, select max of top & left
				dp[i][j] = max(dp[i][j-1],dp[i-1][j-1])
	print('HERE;',dp)
	return dp[n1][n2]
s1 = "lmnop"
s2 =  "lmmnoop"
s1="BCDAACD"
s2="ACDBAC"



def lcs(X , Y):
	# find the length of the strings
	m = len(X)
	n = len(Y)

	# declaring the array for storing the dp values
	L = [[None]*(n+1) for i in range(m+1)]

	"""Following steps build L[m+1][n+1] in bottom up fashion
	Note: L[i][j] contains length of LCS of X[0..i-1]
	and Y[0..j-1]"""
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j] , L[i][j-1])

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
	print(L)
	return L[m][n]
#end of function lcs


# Driver program to test the above function
s1 = "BCDAACD"
s2 = "ACDBAC"
# print(longest_common_subsequence(s1,s2,len(s1),len(s2)))
# print(lcs(s1,s2))



