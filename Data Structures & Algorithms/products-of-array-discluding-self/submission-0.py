class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [1] * nums_len
        prefix = [1] * nums_len
        suffix = [1] * nums_len
        for i in range(nums_len - 1):
            prefix[i + 1] = prefix[i] * nums[i]
            suffix[nums_len - i - 2] = suffix[nums_len - i - 1] * nums[nums_len - i - 1]
        for i in range(nums_len):
            result[i] = prefix[i] * suffix[i]
        return result
