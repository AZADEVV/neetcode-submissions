class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = defaultdict(int)

        for ch in s:
            d[ch] += 1

        longest = 0
        a = 0
        for val in d.values():
            if val % 2 == 0:
                longest += val
            else:
                longest += val - 1
                a = 1

        return longest + a