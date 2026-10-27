class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_len = m + n
        i, j = 0, 0
        merged = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1
        mid = (total_len)//2
        if total_len % 2 == 1:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid])/2.0