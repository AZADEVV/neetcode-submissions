class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(n)}


        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        arr = []

        def dfs(i, length):

            if i in visit: return length

            visit.add(i)

            for nei in adj[i]:
                dfs(nei, length + 1)

            arr.append(length)
            

        res_i = []
        res_v = []
        for i in range(n):
            visit = set()
            arr = []
            dfs(i, 0)
            res_i.append(i)
            res_v.append(max(arr))

        minn = min(res_v)
        r = []
        for i in range(len(res_v)):
            if res_v[i] == minn:
                r.append(res_i[i])

        return r

        