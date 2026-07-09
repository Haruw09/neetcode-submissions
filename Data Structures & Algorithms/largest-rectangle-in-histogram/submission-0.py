class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        extended = heights + [0]
        stack = []
        max_area = 0
        for i, height in enumerate(extended):
            while stack and extended[stack[-1]] > height:
                rect_height = extended[stack.pop()]
                left_border = stack[-1] if stack else -1
                width = i - left_border - 1
                area = rect_height * width
                max_area = max(area, max_area)

            stack.append(i)
        
        return max_area