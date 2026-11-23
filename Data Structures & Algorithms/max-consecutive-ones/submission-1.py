class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        maxx = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            maxx = max(count, maxx)

        return maxx 

                