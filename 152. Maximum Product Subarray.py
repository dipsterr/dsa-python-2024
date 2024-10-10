nums = [2,-1,-8, 0]
from sys import maxsize


def maxprod(nums):

    currmax, currmin = nums[0], nums[0]
    maxprod = nums[0]

    for i in range (1, len(nums)):
        currmax, currmin = max(nums[i], currmax*nums[i], currmin*nums[i]), min(nums[i], currmax*nums[i], currmin*nums[i])
        maxprod = max(currmax, currmin, maxprod)
        
    return maxprod

print( maxprod(nums))