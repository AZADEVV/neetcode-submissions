class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        second_l = 0
        second_r = len(nums) - 1

        m = l
        while second_l <= second_r:

            if target == nums[m]:
                return m
            elif nums[second_r] < target:
                second_r = m - 1
            else:
                second_l = m + 1
           
            m = (second_l + second_r) // 2

        return -1


# [1, 2t, 3, 4m, 5, 6, 7]   true
# [5, 6, 7, 1m, 2t, 3, 4]   true
# [4, 5, 6, 7m, 1, 2t, 3]   false   target < nums[m]
#
# [1, 2, 3, 4m, 5, 6t, 7]   true
# [5, 6t, 7, 1m, 2, 3, 4]   false   target < nums[m]
# [4, 5, 6t, 7m, 1, 2, 3]   true
#
#
# [1, 2t, 3, 4m, 5, 6, 7]   true
# [5, 6, 7, 1m, 2t, 3, 4]   true
# [4, 5, 6, 7m, 1, 2t, 3]   true
#
# [1, 2, 3, 4m, 5, 6t, 7]   true
# [5, 6t, 7, 1m, 2, 3, 4]   false   target < nums[m]
# [4, 5, 6t, 7m, 1, 2, 3]   false   nums[m] < nums[r]



