class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        queue = deque(bills)
        fives = 0
        tens = 0

        while queue:
            bill = queue.popleft()

            if bill == 5:
                fives += 1
            
            print(fives, tens)
            if bill == 10:
                if not fives: return False
                fives -= 1
                tens += 1

            if bill == 20:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True

                