from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        n = len(nums)
        l = 0
        count = 0
        prod = 1

        for i in range(n):
            prod *= nums[i]
            while (prod >= k):
                prod /= nums[l]
                l+=1
            count+=(i-l+1)
        return count

if __name__ == "__main__":
     nums = [10,5,2,6]
     k = 100
     print(Solution().numSubarrayProductLessThanK(nums, k))