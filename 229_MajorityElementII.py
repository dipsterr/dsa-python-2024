nums = [5,5,5,3,3,3,3,2,2,2,2]

def majorityElement(nums) :
    result = []
    n = len(nums)
    hashmap= {}
    nums.sort()
    for i in range (n):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
        else:
            hashmap[nums[i]]=1

    for key, value in hashmap.items():
        if value>n/3:
            result.append(key)

    # result.sort()

    return result


    

print(majorityElement(nums))


