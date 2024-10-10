from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]):
        adj = defaultdict(list) #hasmap to store destination and cost
        for src, dest, curr_cost in zip(original, changed, cost):
            adj[src].append((dest, curr_cost))

        def dikjstra(src):
            heap = [(0, src)]
            min_cost_map = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_map:
                    continue
                min_cost_map[node] = cost
                for nei_cost, nei in adj[node]:
                    heapq.heappush(heap, (nei_cost + cost, nei))
            return min_cost_map

        min_cost_maps = {c:dikjstra(c) for c in set(source)}
        res = 0
        for src, dest in zip(source, target):
            if dest not in min_cost_maps[src]:
                return -1
            res += min_cost_maps[src][dest]
        return res

if __name__ == "__main__":
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]
    res = Solution().minimumCost(source, target, original, changed, cost)
    print(res)