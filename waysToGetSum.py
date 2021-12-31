coins = [3,5,10]
#coins = [1,3,5]
n = len(coins)
desiredSum = 15

dp = [0]*(desiredSum+1)
dp[0] = 1

def orderMatters():
    #Counts 3,5 and 5,3 as 2 different
    for i in range(1,len(dp)):
        for coin in coins:
            if i-coin>=0:
                dp[i] += dp[i-coin]
            print(i,coin,dp)
    
def orderDoesntMatter():
    #Counts 3,5 and 5,3 as 2 same
    for coin in coins:
        for i in range(coin,len(dp)):    
            if i%coin==0 or dp[i-coin]>0:
                dp[i] += 1
            print(coin,i,dp)

orderDoesntMatter()
    
    
