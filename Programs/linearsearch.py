#Check each element one by one and pick the smallest repeatedly.
#Like choosing the smallest item from a list again and again until everything is sorted.


def linearsearch(a):
    for i in range(len(a)):
      if a[i] == 3:
        print(" element found", i)
        return i
    else:
         print ("element not found") 


a = [1,5,6,0,8]
linearsearch(a)

