# def printDuplicates(arr, n): 
  
#     fl = 0; 
  
#     for i in range (0, n):  
#       if (arr[arr[i] % n] >= n):  
  
#             if (arr[arr[i] % n] < 2 * n):  
#                 print(arr[i] % n, end = " ") 
#                 fl = 1; 
#         arr[arr[i] % n] += n; 
#     if (fl == 0): 
#         print("-1") 
  
# # Driver Function 
# arr = [ 1, 6, 3, 1, 3, 6, 6 ]; 
# arr_size = len(arr); 
# printDuplicates(arr, arr_size);

# Dynamic Programming implementation of LCS problem

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
X = "BCDAACD"
Y = "ACDBAC"
print ("Length of LCS is ", lcs(X, Y) )

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
