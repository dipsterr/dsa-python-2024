from typing import List


class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        curr =  nums[0]
        prev = nums[0]
        count = 0
        if nums[0] & nums[1] == 0:
            curr = nums[1]
        
        for i in range (1, len(nums)):
            if curr & nums[i] > 0:
                curr = curr & nums[i]
                count +=1
            else:
                continue

        return count+1


if __name__ == "__main__":
    candidates = [40,35,37,9,32,1,84,48,85,75,94,36,58,85,8,6,91,3,9,69,27,41,99,14,89,18,48,1,42,65,81,46,60,45,64,56,72,40,9,58,23,82,41,27,79,52]
    print(Solution().largestCombination(candidates))
