from typing import List
import sys


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]):
        N, M = len(matrix), len(matrix[0])
        
        rowMinMax = -sys.maxsize
        for i in range(N):
            rowMin = min(matrix[i])
            rowMinMax = max(rowMinMax, rowMin)

        colMaxMin = sys.maxsize
        for i in range(M):
            colMax = max(matrix[j][i] for j in range(N))
            colMaxMin = min (colMaxMin, colMax)

        if rowMinMax == colMaxMin:
            return [rowMinMax]
        else:
            return []
        
            
            

                

        # return result


if __name__ == "__main__":

    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

    res = Solution().luckyNumbers(matrix)
    print(res)