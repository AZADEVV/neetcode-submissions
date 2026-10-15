class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        res = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in seen:
                    res.append(grid[i][j])
                seen.add(grid[i][j])

        for i in range(1, len(seen) + 2):
            if i not in seen:
                res.append(i)

        return res