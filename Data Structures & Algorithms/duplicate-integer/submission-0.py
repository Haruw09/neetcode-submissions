class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set(nums)
        if len(nums) == len(unique_values):
            return False
        else:
            return True