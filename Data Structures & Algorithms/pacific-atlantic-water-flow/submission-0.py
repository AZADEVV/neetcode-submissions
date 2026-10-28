class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        def dfs(i, j, visit, prevHeight):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i, j) in visit or heights[i][j] < prevHeight:
                return

            visit.add((i, j))

            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])


        for i in range(len(heights)):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, len(heights[0]) - 1, atl, heights[i][len(heights[0]) - 1])

        for j in range(len(heights[0])):
            dfs(0, j, pac, heights[0][j])
            dfs(len(heights) - 1, j, atl, heights[len(heights) - 1][j])

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res