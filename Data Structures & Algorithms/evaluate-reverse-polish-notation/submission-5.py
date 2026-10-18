class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        for ele in tokens:
            if ele == '+':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y + x)
            elif ele == '-':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y - x)
            elif ele == '*':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y * x)
            elif ele == '/':
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(int(y / x))
            else:
                stack.append(ele)
        return stack[-1]
        