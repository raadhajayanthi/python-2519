def selectionsort(numbers):
    for i in range (len(numbers)):
        min_num = i
        for j in range(i+1,len(numbers)):
            if numbers[j] < numbers[min_num]:
               min_num = j
        numbers[i], numbers[min_num] = numbers[min_num], numbers[i]


    print("selectionsort: ", numbers)   

selectionsort([5,6,1,2,9])         



