#Insert each element into its correct place.
#Like sorting playing cards in your hand: pick one card and place it where it fits.


def insertionsort(list):
    for i in range (1,len(list)):
      k = list[i]
      j= i-1
      while j>=0 and  list[j]>k:
         list[j+1] = list[j]
         j = j-1
      list[j+1] = k
         
         
    print("insertion sorting: " ,list) 
insertionsort([5,2,4,6])         
         
         
         





