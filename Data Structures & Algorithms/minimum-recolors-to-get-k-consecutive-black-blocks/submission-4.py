class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if len(blocks) == 1:
            if blocks[0] == "W": return 1
            else: return 0
        l = 0
        r = 0
        white = 0
        black = 0
        minn = float("inf")

        while r < len(blocks):
            if blocks[r] == "W":
                white += 1
            else:
                black += 1
            
            r += 1

            if r - l > k:
                if blocks[l] == "W":
                    white -= 1
                else:
                    black -= 1                
                l += 1

            if r - l == k:
                minn = min(minn, white)
            print(l, r, white, black, minn)

        return minn