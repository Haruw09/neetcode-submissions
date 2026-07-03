class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        left_max = [0] * nums_len
        right_max = [0] * nums_len
        
        right_max[nums_len - 1] = nums[nums_len - 1]

        for i in range(1, nums_len):
            if i % k == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(nums[i], left_max[i - 1])
            
            j = nums_len - i - 1
            if j % k == 0:
                right_max[j] = nums[j]
            else:
                right_max[j] = max(nums[j], right_max[j + 1])

        result = [0] * (nums_len - k + 1)
        for i in range(0, nums_len - k + 1):
            result[i] = max(right_max[i], left_max[i + k - 1])

        return result