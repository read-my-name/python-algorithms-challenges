from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        
        # Function to find the root of node i
        def find(i):
            if parent[i] == i: 
                return i
            else:
                res = find(parent[i])
                parent[i] = res  # Path compression
                return res

        # Function to union two nodes i and j
        def union(i, j): 
            parent[find(i)] = find(j)  # Always attach tree of i to tree of j

        # Union all edges
        for e in edges:
            union(e[0], e[1])
        
        # Check if source and destination have the same root
        return find(source) == find(destination)

    
if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(Solution().validPath(n, edges, source, destination)) # False
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(Solution().validPath(n, edges, source, destination)) # True








