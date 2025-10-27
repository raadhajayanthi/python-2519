def sorting_numbers(numbers):

    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

    print("sorted numbers: " ,numbers)

sorting_numbers([1,9,10,11,3,2])  
sorting_numbers([-1,-9,-10,11,3,2])  





        

