from sys import stdin   
def subset_sum_2(arr,n,total):
    dp = [0]*(total+1)
    tempTotal = 0
    arr.sort()
    for element in arr:
        tempTotal += element
        
        for i in range(element,tempTotal+1):
           if i<=total and (element == i or dp[i-element]):
               dp[i] += 1
           print(element,i,dp[1:])
    return 1 if dp[-1]>0 else 0

def subset_sum(arr,n,total):
    dp = [[False]*(total+1) for i in range(n)]
    dp[0][0] = True
    #print(dp,len(dp))
                
    for i,element in enumerate(arr):
        for j in range(element,len(dp[0])):
            if element==j or dp[i-1][j-element]:
                dp[i][j] = True
                print(element,i,j,dp)
    return dp[-1][-1]

if __name__=="__main__":
    arr = [3,5,10] #list(map(int,stdin.readline().split()))
    #n = int(stdin.readline())
    total = 11 #int(stdin.readline())
    print(subset_sum(arr,len(arr),total))
