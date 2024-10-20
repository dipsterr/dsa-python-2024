class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        set1 = set(nums1)
        set2 = set(nums2)
        for num in set1:
            if num in set2:
                result.append(num)
        return result