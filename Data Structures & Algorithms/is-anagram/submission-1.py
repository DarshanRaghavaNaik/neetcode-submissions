class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_array = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            freq_array[index] += 1
        for c in t:
            index = ord(c) - ord('a')
            freq_array[index] -= 1

        for v in freq_array:
            if v != 0:
                return False
        return True 