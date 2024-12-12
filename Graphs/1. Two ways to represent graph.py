from collections import deque


n = int(input("Enter n: "))

#Graph Representation as Matrix
graph = [[0]*n for _ in range(n)]
for i in range(n):
    u = int(input())
    v = int(input())
    graph[u][v]=1
    graph[v][u]=1

#Graph Representation as List
m = int(input())
adj = [[] for _ in range(n+1)]
for i in range(m):
    u = int(input())
    v = int(input())
    adj[u].append(v)
    adj[v].append(u)

print(adj)


queue = deque()
print(queue)