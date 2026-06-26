class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        highest_left = height[left]
        highest_right = height[right]

        result = 0

        while left < right:
            if highest_left < highest_right:
                left += 1
                highest_left = max(height[left], highest_left)
                result += (highest_left - height[left])
            else:
                right -= 1
                highest_right = max(height[right], highest_right)
                result += (highest_right - height[right])
        
        return result
                
