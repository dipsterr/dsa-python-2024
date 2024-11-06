class Solution(object):
    def canSortArray(self, nums):
        setBits = bin(nums[0]).count('1')
        currMax = nums[0]
        currMin = nums[0]

        prevMax = float("-inf")

        for i in range(1, len(nums)):
            if setBits == bin(nums[i]).count("1"):
                currMax = max(currMax, nums[i])
                currMin = min(currMin, nums[i])
            else:
                if currMin < prevMax:
                    return False
                prevMax = currMax
                currMax = nums[i]
                currMin = nums[i]
                setBits = bin(nums[i]).count("1")
            
        if currMin < prevMax:
            return False
            
        return True
        