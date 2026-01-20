def quicksort(a):
   if len(a) <= 1:
     return a
   else:  
     pivot_element = a[-1]
     left = []
     for x in a[:-1]:
      if x <= pivot_element:
        left.append(x)
     right = []
     for x in a[:-1]:
      if  x >= pivot_element:
       right.append(x)
     return quicksort(left) + [pivot_element] + quicksort(right)


a = [5,2,9,1,7]
sortedlist = quicksort(a)
print ("quicksort", sortedlist)
