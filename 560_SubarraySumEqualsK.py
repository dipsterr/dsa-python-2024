nums = [1,0,-1,1]

k = 0

from collections import Counter

def subarray(nums, k):
    result = 0
    hashmap= {}
    n = len(nums)
    sum = 0


    for i in range (n):

        sum += nums[i]

        if (sum == k):
            result +=1

        prevSum = sum - k
        
        if prevSum in hashmap:
            result += hashmap[prevSum]

        hashmap[sum] = i     

    return result

    # for num in nums:
    #     sum = sum + num
    #     prevSum = sum -k

    #     if prevSum in d:
    #         result = result + d[prevSum]

    #     if sum not in d:
    #         d[sum] = 1
    #     else:
    #         d[sum] = d[sum] + 1

    # return result

print(subarray(nums, k))