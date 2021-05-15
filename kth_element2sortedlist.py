import random
import math
#Using Sorting

#Sort the array arr
#Take two pointers, l and r, both pointing to 1st element
#Take the difference arr[r] – arr[l]
#If value diff is K, increment count and move both pointers to next element
#if value diff > k, move l to next element
#if value diff < k, move r to next element
#return count


def countPairsWithDiffK(arr,n,k): 
  
    count =0
      
    # Sort array elements 
    arr.sort()  
  
    l =0
    r=0
  
    while r<n: 
        if arr[r]-arr[l]==k: 
            count+=1
            l+=1
            r+=1
              
        # arr[r] - arr[l] < sum 
        elif arr[r]-arr[l]>k:  
            l+=1
        else: 
            r+=1
    return count 
  
# Driver code 
if __name__=='__main__': 
    arr = [1, 5, 3, 4, 2] 
    n = len(arr) 
    k = 3
    print("Count of pairs with given diff is", countPairsWithDiffK(arr, n, k)) 
