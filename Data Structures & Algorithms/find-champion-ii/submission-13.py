class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        if len(edges) < n - 1: return -1
 
        keys = set()
        vals = set()
        al = set()

        for edge in edges:
            keys.add(edge[0])
            vals.add(edge[1])
            al.add(edge[0])
            al.add(edge[1])
        
        for i in range(n):
            if i not in al: return -1

        champ = -1
        
        count = 0
        for key in keys:
            if key not in vals:
                if count > 0: return -1
                champ = key
                count += 1
        return champ