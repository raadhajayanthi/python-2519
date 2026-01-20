
#Place each number into a binary tree, then read it in sorted order.
#Or sometimes means Binary Search + Sort logic: divide the list into two halves repeatedly.


def binarysearch(a):
    a.sort()
    print("sorted elements" ,a)
    target = 30
    low = 0
    high = len(a) - 1
    
    
    while low <= high:
     middle = (low+high) // 2
     if target == a[middle]:
        print("element found at index", middle)
        return middle
     elif target < a[middle]:
        high = middle - 1    
     else:
         low = middle + 1  
 
    return -1
a = [10,5,30,20,60]
x = binarysearch(a)
       
    









