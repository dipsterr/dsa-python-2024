nums1 = [1,8,9,10,12]

nums2 = [2,3,5,6]


def merge (nums1, nums2):
    # m = len(nums1)
    # nums1 = nums1 + nums2
    # n = len(nums1)
    # i = 0
    # while (i<n and m<n):
    #         if ( nums1[i]<nums1[m]):
    #             nums1[i] = nums1[i]
    #             i+=1
    #         else:
    #             nums1[i], nums1[m] = nums1[m], nums1[i]
    #             m+=1
    # return nums1

    m = len(nums1)-1
    n = 0
    while (m>=0 and n <len(nums2)):
        if nums1[m]>nums2[n]:
            nums1[m], nums2[n] = nums2[n], nums1[m]
        m-=1
        n+=1
    nums1.sort()
    nums2.sort()
    return nums1+nums2

    

print(merge(nums1, nums2))