#find Ways To Climb N Stairs, K at a time
def findWaysToClimbStairs(dp,n,k):
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len(dp)):
        for j in range(1,k+1):
            dp[i] += dp[i-j]
    return dp[n]

n=3
k=3
arr = [0]*(n+1)
print(findWaysToClimbStairs(arr,n,k))
