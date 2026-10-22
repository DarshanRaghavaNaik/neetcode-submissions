class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minval = nums[0]
        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r] and nums[mid] <= minval:
                minval = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return minval