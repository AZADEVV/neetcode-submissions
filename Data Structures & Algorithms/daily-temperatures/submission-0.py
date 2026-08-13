class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        count = 0
        for i, temp in enumerate(temperatures): # 5, 40

            while stack and temperatures[stack[-1]] < temp: # 36 < 40
                index = stack.pop()
                result[index] = (i - index) # result[3]
                # [1, 0, 1, 0, 1, 0, 0]


            stack.append(i) # [1, 3]


        return result