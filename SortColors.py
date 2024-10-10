nums = [2,0,2,1,1,0]

def sortcolors(nums):
    index=0
    for i in range(len(nums)):
        if (nums[i]==0):
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp
            index+=1
    for i in range(index, len(nums)):
        if (nums[i]==1):
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp
            index+=1

    return nums

print(sortcolors(nums))
            
        
