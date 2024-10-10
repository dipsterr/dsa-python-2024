from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]):
        ROWS, COLS = len(rowSum), len(colSum)

        res = [[0] * COLS for _ in range(ROWS)]

        for r in range (ROWS):
            res [r][0] = rowSum[r]

        for c in range(COLS):
            curColSum = 0
            for r in range(ROWS):
                curColSum += res[r][c]

            r = 0
            while curColSum > colSum[c]:
                diff = curColSum - colSum[c]
                maxShift = min(res[r][c], diff)
                res[r][c] -= maxShift
                res[r][c+1] += maxShift
                curColSum -= maxShift
                r+=1
        return res

