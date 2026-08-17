class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        mini = math.inf
        while l <= r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
            
            mini = min(nums[m], mini)

        return mini


#   [1, 2, 3, 4, 5]     
#   [5, 1, 2, 3, 4]
#   [4, 5, 1, 2, 3]
#   [3, 4, 5, 1, 2]
#   [2, 3, 4, 5, 1]
