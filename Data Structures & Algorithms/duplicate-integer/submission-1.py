class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()
        for num in nums:
            if num in unique_values:
                return True
            else:
                unique_values.add(num)
                
        return False