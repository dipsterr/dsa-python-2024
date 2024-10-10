from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]):
        return sorted(target) == sorted(arr)




if __name__ == "__main__":

    target = [1,2,3,4]
    arr = [2,4,1,3]
    res = Solution().canBeEqual(target, arr)
    print(res)