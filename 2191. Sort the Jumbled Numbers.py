from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]):
        pairs = []
        for i, n in enumerate(nums):
            n = str(n)
            mappedNum = 0
            for char in n:
                mappedNum *= 10
                mappedNum += mapping[int(char)]
            pairs.append((mappedNum, i))

        pairs.sort()
        return [nums[p[1]] for p in pairs]
            
            

 

if __name__ == "__main__":
    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = [991,338,38]
    res = Solution().sortJumbled(mapping, nums)
    print(res)
