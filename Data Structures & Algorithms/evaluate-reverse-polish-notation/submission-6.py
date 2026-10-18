class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
                stack.append(int(ele))
        return stack[-1]
        