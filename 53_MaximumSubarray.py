

import sys
nums = [-2,3,4,-1,5,-4]

def largestSubarray(nums):
    maxSum = -sys.maxsize
    currSum = 0
    start, end, count = 0,0,0
    n = len(nums)
    for i in range(n):
        currSum += nums[i]

        if (maxSum < currSum):
            maxSum = currSum
            start = count
            end = i
        
        if (currSum < 0):
            currSum = 0
            count = i+1

    # nums[ :] = nums[start:end+1]
        
    return maxSum

    


print(largestSubarray(nums))

    

