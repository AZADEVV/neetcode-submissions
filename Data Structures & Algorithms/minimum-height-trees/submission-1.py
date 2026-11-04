class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(n)}


        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        arr = []

        def dfs(i, prev, length):

            if i in visit: return length
            # if i == prev: return
            # print(i, adj[i], length)

            visit.add(i)

            for nei in adj[i]:
                cur_length = dfs(nei, i, length + 1)

            arr.append(length)
            

        res_i = []
        res_v = []
        for i in range(n):
            visit = set()
            arr = []
            dfs(i, -1, 0)
            # print(arr)
            res_i.append(i)
            res_v.append(max(arr))

        minn = min(res_v)
        r = []
        for i in range(len(res_v)):
            if res_v[i] == minn:
                r.append(res_i[i])

        # print(f'{res_i=}, {res_v},{r=}, {minn=}')
        return r

        