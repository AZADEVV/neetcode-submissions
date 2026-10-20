class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(i, p):
            if i == n * 2:
                stack = []
                for char in p:
                    if char == '(':
                        stack.append(char)
                    else:
                        if not stack: return
                        top = stack.pop()
                        if top != '(': return

                if len(stack) == 0:
                    res.append(''.join(p))
                    return
                else:
                    return
            
            
            p.append('(')

            backtrack(i + 1, p)

            p.pop()

            p.append(')')

            backtrack(i + 1, p)

            p.pop()
        

        backtrack(0, [])

        return res

