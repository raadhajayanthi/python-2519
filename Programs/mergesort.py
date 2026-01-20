#Divide the list into small parts, sort them, then join (merge) them back.
#Like cutting papers into pieces, sorting each small piece, and then combining them neatly.


def mergesort(a):
    if len(a) > 1:
       mid = len(a)//2
       left = a[:mid]
       right = a[mid:]
       print("Left half:", left)
       print("Right half:", right)

       mergesort(left)
       mergesort(right)

       i = 0
       j = 0
       k = 0
       while i < len(left) and j < len(right):
            if left[i] < right[j]:
              a[k] = left[i]
              i = i + 1
            else:
               a[k] = right[j]
               j = j + 1
            k = k + 1        

       while i < len(left):
           a[k] = left[i]
           i = i + 1
           k = k + 1

       while j < len(right):
           a[k] = right[j]
           j = j + 1
           k = k + 1    

a = [7,5,9,1,6]

mergesort(a)
print("Merging:", a)



