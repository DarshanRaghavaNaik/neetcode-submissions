class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        for c in s:
            seen[c] = seen.get(c,0) + 1
        
        for c in t:
            if c not in seen:
                return False
            seen[c] = seen.get(c,0) - 1


        for value in seen.values():
            if value != 0:
                return False
        return True
