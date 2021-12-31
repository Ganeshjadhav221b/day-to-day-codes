arr = [-10,5,0,3,1]
arr.sort()
search = 3
print(arr)
def bSearch(arr,l,r):
    mid = (l+r)//2
    if arr[mid] == search:
        return mid
    elif arr[mid]>search:
        mid = bSearch(arr,l,mid-1)
        return mid
    else:
        mid = bSearch(arr,mid+1,r)
        return mid
i = bSearch(arr,0,len(arr)-1)
        
print(i)
