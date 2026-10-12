class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        s3 = sorted(s1)
        for i in range(len2 - len1 + 1):
            current_window = sorted(s2[i:i+len1])
            if current_window == s3:
                return True
        return False
        