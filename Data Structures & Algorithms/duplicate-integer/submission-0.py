class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dublicate = False

        for _ in nums:
            d = nums.pop()
            if d in nums:
                has_dublicate = True

        return has_dublicate