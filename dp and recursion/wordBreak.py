def wordBreak():
    dictionary = ["lee","code","er"]
    word = "leetcode"
    n = len(word)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(n):
        for j in range(i,n):
            if dp[i] and word[i:j+1] in dictionary:
                dp[j+1] = True
            print(i,j,dp[i],word[i:j+1],dp)
    return dp[-1]

print(wordBreak())
