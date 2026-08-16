class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
#        piles.sort(reverse=True)

#        extra_h = h - len(piles)

#        while extra_h > 0:
#            piles[]

        hours = 0

        l = 1
        r = max(piles)
        min_hours = math.inf
        k = 0

        while l <= r:
            middle = (l + r) // 2
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / middle)

            if hours <= h:
                min_hours = min(hours, min_hours)
                r = middle - 1
                k = middle
            else:
                l = middle + 1

            hours = 0
        
        return k





# [1, 2, 3, 4]  9
# [4, 3, 2, 1]  9

# [10, 25, 23, 10, 4]  
#
# h = 4                                  k = 25 (max of list)
# h = 5       25 / 10 = 3     2 < 3      k = 25 (second max of list)
# h = 6       25 / 10 = 3     3 = 3      k = 10
#
# h = 51      51 / 51 = 1                k = 1      51
# h = 50      51 / 50 = 2                k = 2      100
# h = 26      51 / 26 = 2                k = 2      52
# h = 25      51 / 25 = 3                k = 3      75                

# h = 4       62 / 4 = 16 


# m = 25
# n = 4



