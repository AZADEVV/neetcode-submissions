class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = (1 + len(nums)) * len(nums) // 2
        summ = sum(nums)

        return S - summ