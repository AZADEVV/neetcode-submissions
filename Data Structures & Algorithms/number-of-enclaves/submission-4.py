
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            count = 1

            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        total_land = 0
        border_land = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: total_land += 1

                if (r == 0 or r == rows - 1 or
                    c == 0 or c == cols - 1 and
                    grid[r][c] == 1):
                    border_land += dfs(r, c)

        return total_land - border_land
