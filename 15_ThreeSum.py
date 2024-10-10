nums = [1,1,1,1]

def threeSums(nums, target):
    nums = sorted(nums)
    n = len(nums)
    result = []
    
    


    hashmap = {}

    for i in range(n):
        hashmap[nums[i]] = i


    for i in range(n):
        j = i+1
        k = n-1
        while (j<k):
            sum = nums[i]+nums[j]+nums[k]
            if ((target-sum) in hashmap and nums[i]!=nums[j]!=nums[k]!=nums[hashmap[target-sum]]):
                result.append([nums[i], nums[j], nums[hashmap[target-sum]], nums[k]])
                j+=1
                k-=1
            elif (sum<0):
                j+=1
            elif (sum>0):
                k-=1

    lists = [list(t) for t in set(tuple(sorted(lst)) for lst in result)]

    return lists



# ans = threeSums(nums, 0)
# print(ans)
# # print(len(result))

# # for it in ans:
# #         print("[", end="")
# #         for ele in it:
# #             print(ele, end=" ")
# #         print("]", end=" ")

def fourSum(nums, target):
    nums = sorted(nums)
    n = len(nums)
    result = []

    if (n < 4):
        return 0
    
    hashmap = {}

    for i in range(n):
        hashmap[nums[i]] = i


    for i in range(n):
        j = i+1
        k = n-1
        while (j<k):
            sum = nums[i]+nums[j]+nums[k]
            if ((target-sum) in hashmap and i!=hashmap[target-sum] and j!=hashmap[target-sum] and k!=hashmap[target-sum]):
                result.append([nums[i], nums[j], nums[hashmap[target-sum]], nums[k]])
                

                j+=1
                k-=1
            elif (sum<0):
                j+=1
            elif (sum>0):
                k-=1
    
    lists = [list(t) for t in set(tuple(sorted(lst)) for lst in result)]

    return lists


# ans = fourSum(nums, 4)


# print(ans)

def triplet(nums, target):
    nums.sort()

    ans  = []

    for i in range(len(nums)-3):
        if(i>0 and nums[i] == nums[i-1]):
            continue

        for j in range(len(nums)-2):

            if(j>i+1 and nums[j] == nums[j-1]):
                continue

            k = j+1

            l = len(nums)-1

 

            while k<l:

                sum1 = nums[i]+nums[j]+nums[k]+nums[l]

                if(sum1<target):

                    k+=1

                elif(sum1>target):

                    l-=1

 

                else:

                    ans.append([nums[i],nums[j],nums[k],nums[l]])

 

                    k+=1

                    l-=1

 

                    while k<l and nums[k] == nums[k-1]:
                        k+=1

                    while k<l and nums[l] == nums[l-1]:
                        l-=1

    return ans


ans = [0,0,0,0]
print(triplet(ans, 0))




 