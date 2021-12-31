
def ways_to_get_sum(arr,n,total):
    #order does not matter'
    #no infinite supply of coins
    #print(total)
    dp = [0]*(total+1)
    dp[0] = 1
    for i in range(1,len(dp)):
        for element in arr:
            if i//element == 1 :#or dp[i-element]>0:
                dp[i] += 1
    print(dp,total)
    return dp[total]>0


def get_equal_sum_partition(arr,n):
    total = round(sum(arr))
    if total&1 == 1:
        return False
    total //= 2
    return ways_to_get_sum(arr,n,total)>0

if __name__=="__main__":
    arr = [5,1,4,6]
    print(get_equal_sum_partition(arr,len(arr)))
