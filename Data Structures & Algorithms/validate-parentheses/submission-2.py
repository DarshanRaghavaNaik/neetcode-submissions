from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for b in s:
            if b in hashmap:
                if stack and stack[-1] == hashmap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return len(stack) == 0

    