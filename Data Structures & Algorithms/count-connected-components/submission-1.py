class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i: [] for i in range(n)}

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        count = 0

        def dfs(i):
            if i in visit: return 0

            visit.add(i)

            for nei in adj[i]:
                dfs(nei)

            return 1
        
        for i in range(n):
            count += dfs(i)

        return count
        