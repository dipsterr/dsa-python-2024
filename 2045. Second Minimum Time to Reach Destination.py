from collections import defaultdict, deque

from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int):
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque([1])
        curr_time = 0
        res = -1
        visit_times = defaultdict()
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:
                        return curr_time
                    res = curr_time 
                for nei in adj[node]:
                    nei_time = visit_times[nei]
                    if len(nei_time) == 0 or (len(nei_time) == 1 and nei_time[0] != curr_time):
                        q.append(nei)
                        nei_time.append(curr_time)
            if (curr_time // change) % 2 ==1:
                curr_time += change - (curr_time % change)
            curr_time += time

        



if __name__ == "__main__":
    n = 5
    edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
    time = 3
    change = 5
    res = Solution().secondMinimum(n, edges, time, change)
    print(res)
