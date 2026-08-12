class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = 0
        max_sum = nums[0]
        for num in nums:
            if prev_sum < 0:
                prev_sum = 0

            prev_sum += num
            max_sum = max(prev_sum, max_sum)

        return max_sum