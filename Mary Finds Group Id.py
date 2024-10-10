def find_group_id(nums):
    n = len(nums)
    groupId = 0
    for i in range(n):
        if nums[i]<nums[i+1]:
            groupId +=10
        elif nums[i]>nums[i+1]:
            if i != 0:
                if nums[i-1]<nums[i]:
                    groupId += 5

    return 
# pfrs = [1,5,2,7,8]
pfrs = [13,9,1,3,7,4,2,12,6,5] #90

print(find_group_id(pfrs)) 

