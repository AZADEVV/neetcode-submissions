class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        r = 0

        summ = 0
        minn = float("inf")

        while r < len(nums):
            summ += nums[r]
            r += 1
            while summ >= target:
                summ -= nums[l]
                l += 1
                minn = min(minn, r - l + 1)
        
        return minn if minn != float("inf") else 0