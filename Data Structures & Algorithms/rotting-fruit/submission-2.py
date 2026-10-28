class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minute = 0
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] != 1:
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            
            minute += 1
        
        return minute if fresh == 0 else -1


            