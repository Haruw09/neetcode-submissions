from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_candidates = deque()
        result = [0] * (len(nums) - k + 1)
        left = 0
        for right in range(0, len(nums)):
            while max_candidates and nums[right] > nums[max_candidates[-1]]:
                max_candidates.pop()
            max_candidates.append(right)

            left = right - k + 1
            if max_candidates[0] < left:
                max_candidates.popleft()
            
            if right >= k - 1:
                result[left] = nums[max_candidates[0]]
        
        return result