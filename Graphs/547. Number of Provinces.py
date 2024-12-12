from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = [[]]*len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    adjList[i].append(j)
                    adjList[j].append(i)

        def dfs(node, adjList, visited):
            visited[node] = 1
            for i in adjList[node]:
                if not visited[i]:
                    dfs(i, adjList, visited)

        visited = [0]*len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                count += 1
                dfs(i, adjList, visited)

        return count
        