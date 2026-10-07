class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def recursion(n):
            arr = [int(i) for i in str(n).split()[0]]
            summ = 0
            for a in arr:
                summ += a**2
            
            if summ == 1:
                return True
            if summ in seen:
                return False
            seen.add(summ)

            return recursion(summ)
        
        return recursion(n)
