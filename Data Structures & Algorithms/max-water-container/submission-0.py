class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        maxarea = 0
        minhight = heights[0]
        while l < r:
            minheight = min(heights[l], heights[r])
            area = minheight * (r - l)
            maxarea = max(maxarea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea

        