from queue import Queue
from typing import List


class Solution:
    def bfsOfGraph(self, adj: List[List[int]], V:int) -> List[int]:
        q = Queue()          # Initialize queue
        result = []         # List to store BFS traversal order
        visited = [0] * V   # Initialize visited array

        q.put(0)            # Add the starting vertex (0) to the queue
        visited[0] = 1      # Mark it as visited

        while q.qsize() != 0:  # While there are elements in the queue
            f = q.queue[0]      # Get the front of the queue without removing it
            result.append(f)    # Add to the result list
            q.get()             # Remove the element from the queue
            
            if len(adj[f]) == 0:  # If no neighbors, skip
                continue
            else:
                for i in adj[f]:  # Iterate over neighbors of f
                    if visited[i] == 0:  # If not visited
                        visited[i] = 1   # Mark as visited
                        q.put(i)         # Add to the queue
        return result



if __name__ == '__main__':
    T = int(input()) # Number of test cases
    for i in range(T):
        V = int(input())# Number of vertices
        E = int(input())# Number of edges
        adj = [[] for i in range(V)]# Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj [u].append(v)
            adj[v].append(u)

    ob = Solution()
    ans = ob.bfsOfGraph(adj, V)
    print("' ".join(map(str, ans)))
