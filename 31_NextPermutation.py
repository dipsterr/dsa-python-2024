nums = [2,1,5,4,3,0,0]

def nextper(nums):
    breakk = 0
    for i in range(len(nums)-2, -1, -1):
        if (nums[i]<nums[i+1]):
            # print(nums[i], i)
            breakk = i
            break

    if (breakk == 0):
        nums.reverse()
        return nums
    
    for i in range(len(nums)-1, breakk, -1):
        if (nums[i]>nums[breakk]):
            print(nums[i], i)
            
            nums[i], nums[breakk] = nums[breakk], nums[i]
            break
    # print(nums)
    nums[breakk+1:] = nums[:breakk:-1]
    nums[breakk+1:] = reversed(nums[breakk+1:])

    
    return nums

    
print(nums)
print(nextper(nums))

# for i in range(len(nums)-2, -1, -1):
#     print(i)


