class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        res = 0

        if math.prod(nums) < k:
            return (1 + len(nums)) * len(nums) // 2

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = math.prod(nums[i:j+1])
                if product < k:
                    res += 1
                else:
                    break

        return res



