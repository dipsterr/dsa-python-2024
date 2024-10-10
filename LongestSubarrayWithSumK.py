nums = [1,0,-1,1]
target = 0

def subarray(nums, k):
    n = len(nums)
    sum = 0
    hashmap = {}
    maxLength = 0

    for i in range(n):

        sum += nums[i]

        if (sum == k):
            maxLength = max(maxLength, i+1)
        
        previousSum = sum - k

        if previousSum in hashmap:
            length = i - hashmap[previousSum]
            maxLength = max(maxLength, length)
        
        if sum not in hashmap:
            hashmap[sum] = i

    return maxLength


print(subarray(nums, target))