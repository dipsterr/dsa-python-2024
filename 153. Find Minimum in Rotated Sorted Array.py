num = [6,7,1,2,3,4]
nums1 = [1,2,3,4,5]
nums = [2,3,1]

def findMin(num):
    pivot = 0

    if len(num)==1:
        return num[0]

    for i in range(len(num)-1):
        if num[i-1]>num[i] and num[i]<num[i+1]:
            pivot = num[i]
    if pivot ==0 and num[-1]<num[0]:
        pivot = num[-1]
    
    
    return pivot

print(findMin(nums))