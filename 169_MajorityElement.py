
nums = [2,2,1,1,1,2,2]

def majorityElement(nums):
    hashmap = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
        else:
            hashmap[nums[i]] = 1

        for key, value in hashmap.items():
            if value >= n/2:
                return key

print(majorityElement(nums))