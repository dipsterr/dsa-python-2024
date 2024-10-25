from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(i - hashmap[nums[i]]) <=k:
                return True
            hashmap[nums[i]] = i
        return False


if __name__ == "__main__":
    nums = [1,0,1,1]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))