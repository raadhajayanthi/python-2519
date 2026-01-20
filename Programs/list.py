def list_sorting(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    return nums

nums = [0,1,0,3,12]
nums = list_sorting([0,1,0,3,12])   
print("sorted list", nums)        


    