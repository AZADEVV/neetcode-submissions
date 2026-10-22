class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        if len(edges) < n - 1: return -1
       
        ch = defaultdict(list)

        for edge in edges:
            ch[edge[0]].append(edge[1])
        
        keys = list(ch.keys())
        vals = list(ch.values())

        champ = -1

        arr = []
        for sublist in vals:
            for x in sublist:
                arr.append(x)

        count = 0

        for i in range(len(keys)):
            if keys[i] not in arr:
                if count > 0:
                    return -1
                champ = keys[i]
                count += 1
        
        return champ