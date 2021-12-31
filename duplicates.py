def printDuplicates(arr, n): 
  
    fl = 0; 
  
    for i in range (0, n):  
      if (arr[arr[i] % n] >= n):  
  
            if (arr[arr[i] % n] < 2 * n):  
                print(arr[i] % n, end = " ") 
                fl = 1; 
        arr[arr[i] % n] += n; 
    if (fl == 0): 
        print("-1") 
  
# Driver Function 
arr = [ 1, 6, 3, 1, 3, 6, 6 ]; 
arr_size = len(arr); 
printDuplicates(arr, arr_size);
