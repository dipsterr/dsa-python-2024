from typing import List
import copy

class Solution:
    def dfs(self, sr, sc, matrix, color, image, initial, delRow, delCol):
        matrix[sr][sc] = color
        n = len(matrix)
        m = len(matrix[0])
        for i in range(4):
            newRow = sr + delRow[i]
            newCol = sc + delCol[i]
            if (newRow >= 0 and newRow <n and newCol >=0 and newCol < m 
                and image[newRow][newCol]==initial and matrix[newRow][newCol] != color):
                self.dfs(newRow, newCol, matrix, color, image, initial, delRow, delCol)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        matrix = copy.deepcopy(image)
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         matrix[i][j] = image[i][j]
        initial = image[sr][sc]
        delRow = [-1,0,1,0]
        delCol = [0,1,0,-1]
        self.dfs(sr, sc, matrix, color, image, initial, delRow, delCol)

        return matrix

if __name__=="__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(Solution().floodFill(image, sr, sc, color))