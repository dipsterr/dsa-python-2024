from collections import deque
import copy
from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for i in range(n)]
        q = deque()

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([[i,j], 0])
                    visited[i][j] = 2
                
        tm = 0
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        while (q):
            r = q[0][0][0]
            c = q[0][0][1]
            t = q[0][1]
            tm = max(tm, t)
            q.pop()
            for i in range(4):
                newRow = r+delRow[i]
                newCol = c+delCol[i]
                if (newRow >=0 and newRow < n and newCol >=0 and newCol < m
                    and visited[newRow][newCol] != 2 and grid[newRow][newRow]==1):
                    q.append([[newRow, newCol], t+1])
                    visited[newRow][newCol] = 2
                    print("rotting", visited)

        for i in range (n):
            for i in range(m):
                if (visited[i][j] !=2 and grid[i][j] == 1):
                    return -1
        return tm

        
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))