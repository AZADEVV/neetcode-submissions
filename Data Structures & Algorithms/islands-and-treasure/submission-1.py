class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            i = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == -1 or grid[nr][nc] == 0:
                        continue
                    if grid[r][c] + 1 < grid[nr][nc]:
                        q.append((nr, nc))
                        grid[nr][nc] = grid[r][c] + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)
                    