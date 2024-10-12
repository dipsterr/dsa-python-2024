from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            com = target - nums[i]
            # print(com)
            # print(hashmap[com])
            if com in hashmap and hashmap[com] != i:
                return [i, hashmap[com]]
        return []