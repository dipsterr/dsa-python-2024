

from collections import deque
from typing import List


class Solution:
    def resultsArray(self, arr: List[int], k: int):

        res = []

        Qi = deque()
        for i in range(k):

    
            while Qi and arr[i] >= arr[Qi[-1]]:
                Qi.pop()

            Qi.append(i)

        for i in range(k, len(arr)):
            res.append(arr[Qi[0]])
            # print(str(arr[Qi[0]]) + " ", end="")
            while Qi and Qi[0] <= i-k:
                Qi.popleft()
            while Qi and arr[i] >= arr[Qi[-1]]:
                Qi.pop()
            Qi.append(i)
        res.append(arr[Qi[0]])
        print(str(arr[Qi[0]]))


if __name__ == "__main__":
    arr = [1,2,3,4,3,2,5]
    K = 3
    
    # Function call
    Solution().resultsArray(arr, K)
        
    