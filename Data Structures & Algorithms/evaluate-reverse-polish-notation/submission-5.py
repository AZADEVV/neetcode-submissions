class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        for token in tokens:
            if token in ops:
                if token == '+':
                    res = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == '-':
                    res = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == '*':
                    res = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == '/':
                    res = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[0]