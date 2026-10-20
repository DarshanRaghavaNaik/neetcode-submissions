class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        heights.append(0) #The final 0 forces the remaining bars out of the stack so that we can calculate their areas.

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                maxarea = max(maxarea, area)

            stack.append(i) #We keep these indices so that we can calculate the rectangle's width when a shorter bar appears.
        return maxarea