from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        bitCount = [0] * 32
        currOR = 0
        minLength = float('inf')

        for right in range(len(nums)):
            currOR |= nums[right]

            for bit in range(32):
                if nums[right] & (1<<bit):
                    bitCount[bit] +=1

            while left <= right and currOR >= k:
                minLength = min(minLength, right - left + 1)
                updatedOR = 0
                for bit in range(32):
                    if nums[left] & (1<<bit):
                        bitCount[bit] -=1
                    if bitCount[bit] > 0:
                        updatedOR |= (1<<bit)
                
                currOR = updatedOR
                left +=1


        return minLength if minLength != float('inf') else -1

if __name__ == "__main__":
    nums = [1,2,3]
    k = 2
    print(Solution().minimumSubarrayLength(nums, k))
    