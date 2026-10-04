class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i, summ):
            if summ == target:
                res.append(subset.copy())
                return
            elif summ > target or i == len(nums):
                return

            subset.append(nums[i])
            summ += nums[i]

            backtrack(i, summ)

            subset.pop()
            summ -= nums[i]

            backtrack(i + 1, summ)
        

        backtrack(0, 0)

        return res
