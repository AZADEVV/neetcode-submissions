class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = [str(i) for i in digits]
        num = ''.join(num)
        print(num)

        numInt = str(int(num) + 1)
        result = numInt
        return [i for i in numInt]