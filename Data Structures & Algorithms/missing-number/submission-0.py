class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_idx = len(nums)
        for i, num in enumerate(nums):
            missing_idx ^= i ^ num

        return missing_idx