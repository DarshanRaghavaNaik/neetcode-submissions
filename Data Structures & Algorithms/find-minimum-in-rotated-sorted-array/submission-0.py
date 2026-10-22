class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = max(nums)
        for n in nums:
            if n < minval:
                minval = n
        return minval