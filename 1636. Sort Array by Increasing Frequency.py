from typing import List
from collections import Counter

class Solution:
    def IncreasingFrequencySort(self, nums: List[int]):
        count = Counter(nums)
        sortedDict = sorted(nums, key=lambda x:(count[x], -x))
        return sortedDict

    def decreasingFrequencySort(self, nums: List[int]):
        count = Counter(nums)
        sortedDict = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        res = []
        for element, freq in sortedDict:
            res.extend([element] * freq)
        return res


if __name__ == "__main__":
    nums = [2,3,1,3,2,2,2,10]
    res = Solution().IncreasingFrequencySort(nums)
    print(res)