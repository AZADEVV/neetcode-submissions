class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)








#   4 + 2   6 + 2   8 + 2   10 
#   1 + 2   3 + 2   5 + 2   7 + 2   9 + 2   10
#   0 + 1   1 + 1   2 + 1   3 + 1   4 + 1   5 + 1   6 + 1   7 + 1   8 + 1   9 + 1   10
#   7 + 1   8 + 1   9 + 1   10
#
#   3 