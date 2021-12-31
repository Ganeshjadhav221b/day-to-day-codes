import sys

##arrList = []
##indexList = [1]
##
##
##n = int(input("Enter length: "))
##indexList *= n
##print("Enter elementsL: ")
##for i in range(n):
##    arrList.append(int(input()))
##
##print(arrList)
##for i in range(n):
##    for j in range(0,i):
##        if arrList[i]>arrList[j] and indexList[i]<indexList[j]+1:
##            indexList[i] += 1
##            
##print(max(indexList))

def longIncSubSum():
    #arrList = [5,11,3,15,30,25]
    arrList = [5,11,3,40,50,23]
    n = len(arrList)
    dp = [1]*n
    for i in range(1,n):
        maximum = -sys.maxsize
        for j in range(i-1,-1,-1):
            if arrList[i]>arrList[j] and maximum<dp[j]:
                maximum =  dp[j]
        
        dp[i] += max(0,maximum)
    
    print(dp)
    
longIncSubSum()
