class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        N = len(nums)

        for i in range(1, 2 * N):
            if nums[(i) % N] <= nums[(i + 1) % N]:
                count += 1
            else:
                count = 1
            
            if N == count:
                return True
            
        return N == 1
