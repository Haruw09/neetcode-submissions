class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_len = len(nums)
        prefix = 1
        suffix = 1
        result = nums[0]
        for i in range(nums_len):
            prefix = prefix * nums[i] if prefix else nums[i]
            suffix = suffix * nums[nums_len - 1 - i] if suffix else nums[nums_len - 1 - i]
            result = max(result, prefix, suffix)

        return result
