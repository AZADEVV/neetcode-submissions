class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                ones = 0
            m = max(m, ones)

        return m
