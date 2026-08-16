class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            middle = (l + r) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / middle)

            if hours <= h:
                r = middle - 1
                k = middle
            else:
                l = middle + 1
        
        return k

