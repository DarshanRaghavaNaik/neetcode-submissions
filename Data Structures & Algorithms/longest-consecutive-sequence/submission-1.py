class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxcount = 0
        for num in hashset:
            if num-1 not in hashset:
                count = 0
                cur = num
                while cur in hashset:
                    count += 1
                    maxcount = max(maxcount, count)
                    cur += 1
        return maxcount