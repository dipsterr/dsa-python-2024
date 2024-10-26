

from collections import deque
from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        if k == 1:
            return nums

        for i in range(n - k + 1):
            is_consecutive = True

            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    is_consecutive = False
                    break

            if is_consecutive:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)

        return result
        


if __name__ == "__main__":
    arr = [1,2,3,4,3,2,5]
    K = 3
    
    # Function call
    print(Solution().resultsArray(arr, K))
        
    