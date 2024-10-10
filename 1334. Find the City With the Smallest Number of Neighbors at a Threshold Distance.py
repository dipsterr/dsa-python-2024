from typing import List
from sys import maxsize

class Solution:
    def floyd(self, n: int, dist: List[List[int]]):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (dist[i][k]== maxsize or dist[k][j]==maxsize):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
        pass
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int):
        dist = [[maxsize]* n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for start, end, weight in edges:
            dist[start][end] = weight
            dist[end][start] = weight

        self.floyd(n, dist)
        return self.get_city_with_fewest_reachable(
            n, dist, distanceThreshold)

    def get_city_with_fewest_reachable(
        self, n: int, dist: List[List[int]], distance_threshold: int):

        cntCity = n
        cityNo = -1
        for city in range(n):
            cnt = 0
            for adjCity in range(n):
                if (dist[city][adjCity] <= distance_threshold):
                    cnt+=1
            if (cnt <= cntCity):
                cntCity = cnt
                cityNo = city

        return cityNo


name= input()
age = int(input())
print(f"The name of the person is {name} and the age is {age}.")