class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        premap = {i: [] for i in range(n)}

        for i, j in edges:
            premap[i].append(j)
            premap[j].append(i)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for nei in premap[i]:
                if nei == prev: continue
                if not dfs(nei, i): return False
            
            return True

        return dfs(0, -1) and n == len(visit)