n = 5

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
	res = seen[n]
	if seen[n] == 0:
		res = memoized_fib(n-1,seen) + memoized_fib(n-2,seen)
		seen[n] = res

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
	res = seen[n]
	if seen[n] == 0:
		res = memoized_climbing_stairs(n-1,seen)+memoized_climbing_stairs(n-2,seen)+memoized_climbing_stairs(n-3,seen) 
	seen[n] = res
	return res




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

def mimnimum_cost_path(matrix, m, n):
	maximum = 999  #constant
	right = maximum #temporary initialization
	below = maximum #temporary initialization
	dp = [[maximum]*n]*m
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
			print(i,j,rightIndex,right, belowIndex, below, matrix[i][j],dp[i][j] )
	return dp[0][0]

matrix = [[2,3,4,1],[6,3,8,1],[1,1,0,3],[6,7,4,2]]
# print(mimnimum_cost_path(matrix, len(matrix), len(matrix[0])))
