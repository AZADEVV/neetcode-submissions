class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        water = 0
        while l < r:
            if heights[l] < heights[r]:
                if water < heights[l] * (r - l):
                    water = heights[l] * (r - l)   # 7
                l += 1
            else:
                if water < heights[r] * (r - l):
                    water = heights[r] * (r - l)   # 36
                r -= 1
            
        return water
        