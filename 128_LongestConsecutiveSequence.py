nums = [0,3,7,2,5,8,4,6,0,1]

# def nextper(nums):
#     nums = set (nums)
#     result = 0
#     for i in nums:
#         if (i-1) not in nums:
#             length = 1
#             while (i+length) in nums:
#                 length+=1
#             result = max(result, length)
#     return result

def nextSeq(nums):
    nums = set (nums)
    result = 1
    count = 1
    for i in (nums):
        if (i+1) in nums:
            count +=1
        else:
            count = 1
            
        result = max(result, count)
    return result
    

print(nextSeq(nums))



