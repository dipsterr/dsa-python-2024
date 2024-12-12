
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):

        def dfs(node, adj, visited, result):
            visited[node] = 1             # Mark the node as visited
            result.append(node)           # Add the node to the result

            for i in adj[node]:           # Iterate over all neighbors of the node
                if not visited[i]:        # If the neighbor is not visited
                    dfs(i, adj, visited, result)  # Recursive call for the neighbor

        visited = [0] * len(adj)  # Initialize all nodes as not visited
        start = 0                 # Start DFS from node 0
        result = []               # Initialize the result list

        dfs(start, adj, visited, result)  # Start DFS from the starting node
        return result


if __name__ == '__main__':
    T = 1
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
        print("~")

a = 0

print(not a)