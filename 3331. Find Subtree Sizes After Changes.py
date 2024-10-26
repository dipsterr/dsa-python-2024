from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        newParent = [-1] * n

        def findNewParent(node):
            temp = parent[node]
            while temp != -1 and s[temp] != s[node]:
                temp = parent[temp]

            if temp != -1:
                newParent[node] = temp
            else:
                newParent[node] = parent[node]
            return
        
        for i in range(n):
            findNewParent(i)

        child = [[] for _ in range(n)]
        for char, par in enumerate(newParent):
            if par != -1:
                child[par].append(char)
        subTree = [0]*n
        
        def subTreeSize(node):
            size = 1
            for ch in child[node]:
                size += subTreeSize(ch)
            subTree[node] = size
            return size

        subTreeSize(0)
        return subTree